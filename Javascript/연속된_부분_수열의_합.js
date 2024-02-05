
function solution(sequence, k) {
    var answer = [];
    var left = 0;
    var right = 0;
    var minSum = 1000000001;
    var sum = sequence[0];
    var n = sequence.length;
    sequence.sort((a, b) => { return a-b });
    while(left <= right < n){
        // var sum = sequence.slice(start, end + 1).reduce((acc, val) => acc + val, 0);
        if(left == n && right == n){
            break;
        } 
        if(sum == k){
            answer.push([left, right]);
            sum -= sequence[left++];
        } else {
            // 합이 더 적다면 오른쪽 인자를 늘려서 합하기
            if(sum < k){
                if(right < n) sum += sequence[++right];
            }
            // 합이 더 크다면 왼쪽 인자를 높여서 기존 합에서 빼기
            else {
                if(left < n) sum -= sequence[left++];
            }
        } 
    }
    var start = 0;
    var end = 0;
    for(var i=0; i<answer.length;i++){
        if(answer[i][1] - answer[i][0] < minSum){
            minSum = (answer[i][1] - answer[i][0]);
            start = answer[i][0];
            end = answer[i][1];
        }
    }
    return [start, end];
}