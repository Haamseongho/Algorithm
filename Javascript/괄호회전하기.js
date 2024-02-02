function solution(s) {

    var inputArr = s.split(''); // 문자열 > 배열로 변환 (Queue Shift 이용하기 위함)
    var repeatCount = s.length - 1;
    var result = 0; // 성공여부
    for(var inx=0; inx<repeatCount; inx++){
        var stack = [];  // 올바른 괄호인지 체크하기 위한 스택
        for(var i=0;i<s.length;i++){
            // 소괄호
            if(inputArr[i] === ")"){
                if(stack.includes("(")){
                    stack.pop();
                } else {
                    stack.push(inputArr[i]); // 하나씩 넣기
                }
            } 
            else if(inputArr[i] === "}"){
                if(stack.includes("{")){
                    stack.pop();
                } else {
                    stack.push(inputArr[i]); // 하나씩 넣기
                }
            }
            else if(inputArr[i] === "]"){
                if(stack.includes("[")){
                    stack.pop();
                } else {
                    stack.push(inputArr[i]); // 하나씩 넣기
                }
            }
            else {
                stack.push(inputArr[i]); // 하나씩 넣기
            }
        }         
        if(stack.length === 0){
            result += 1;
        }
        // 반복문 한 번 끝나면 inputArr 쉬프트 이동 진행
        inputArr.push(inputArr.shift());
    }
    
   
    return result;
}

