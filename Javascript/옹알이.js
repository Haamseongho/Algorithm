function solution(babbling) {
    // 4가지로 만들 수 있는 옹알이의 갯수: 4C1 * 4C2 * 4C3 * 4C4
    var answer = 0;// 테스트
    const inputArray = ["aya", "ye", "woo", "ma"];
    for(var i=0;i<babbling.length;i++){
        for(var j=0;j<inputArray.length;j++){
            if(babbling[i] != " "){
                babbling[i] = babbling[i].replaceAll(inputArray[j], " ");
            }
        }
        
        if(babbling[i].trim().length == 0){
            answer += 1;
        }
    }
    
    return answer;
  }
  