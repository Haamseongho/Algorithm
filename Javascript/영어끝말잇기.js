function solution(n, words) {
    var answer = [0, 0];

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다. 
    var mappedByWords = [];
    var circularCount = 0;
    var grade = 0;
    var j = 0;
    for(var i=0;i<words.length;i++){
        // n과 나눴을때 나머지가 없다는 것은 n바퀴가 돈 것이라 설명할 수 있음
        if(j % n == 0){
            circularCount += 1;
        }
        if(i > 0){
            let lastIndex = words[i-1].length - 1;
            // 없는 단어를 말해서 끝나는 경우 (3)
            if(words[i-1].charAt(lastIndex) !== words[i].charAt(0)){
                answer = [];
                grade = (i % n);
                answer.push((grade + 1), circularCount);
                break;
            } 
        }
        // 이미 존재하는 단어를 말해서 끝나는 경우 (4)
        if(mappedByWords.indexOf(words[i]) !== -1){
            answer = [];
            grade = (i % n);
            answer.push((grade + 1), circularCount);
            break;
        } 
       
        // 한 글자인 단어만 말하는 경우 (5)
        if(words[i].trim().length === 1){
            answer = [];
            grade = (i % n);
            answer.push((grade + 1), circularCount);
            break;
        }
        // 값 쌓아둔다~~~ 
        else {
            console.log(` in : ${words[i]}`);
            mappedByWords.push(words[i]);
            j+=1;
        }
        
    }
    
    console.log(answer);
    return answer;
}