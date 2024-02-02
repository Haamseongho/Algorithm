function solution(targets) {
    var answer = 1; // 어차피 한 번은 맞을거라서
    // 우선 오름차순으로 정리를 먼저해야함 그래야 요격으로 쑤실 때에도 좀 더 편함
    targets.sort((a, b) => b[0] - a[0]);
    // 시작 위치, 종료 위치 잡고 해당 범위 내에서 요격미사일 날리는데 end안에서 다음 start가 있으면 요격갯수 늘리기
    var targetPoint = targets[0][0]; // 처음 시작위치 
    
    for(var i = 0; i<targets.length; i++){
        var [start, end] = targets[i];
        if(targetPoint >= end){
            targetPoint = start;
            answer++;
        }
    }
    
    return answer;
}