function solution(people, limit) {
    people.sort((a, b) => { return a-b});
    var i = 0;
    var j = people.length-1;
    for(i=0;i<j;j--){
        if(people[i] + people[j] <= limit){
            i++; // 최소 + 최대 무게로 했을때에도 범위 안이라면 사람을 더 태울 수 있음 
        }    
    }
    return people.length - i; // 인당 하나의 구명보트로 체크했을때 구명보트 전체 수 - 제한 내 태운 횟수
}
