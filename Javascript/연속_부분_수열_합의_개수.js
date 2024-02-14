function solution(elements) {
    elements.sort((a, b) => { return a - b })
    var answer = 0;
    var left = 0; // 왼쪽 인덱스
    var right = 0; // 오른쪽 인덱스 
    var n = elements.length;
    var len = 1; // 길이
    var index = 0; // 길이만큼 돌 수 있는 인덱스를 다 돌았을 때, len 증가
    var hashSet = new Set(); // 동일한 값(경우)은 빼기 위함
    var sum = 0;
    while(len <= n){
        // 왼쪽 인덱스가 끝에 닿거나 (길이가 1), 오른쪽 인덱스가 끝에 닿을 경우 (길이가 2 이상)
        if(index >= n || left >= n) {
            index = 0;
            len += 1;
            left = 0;
            right = left + (len - 1); // 길이만큼 띄워주기
            console.log(`left: ${left}, right: ${right}`);
        }
        // 길이가 1인건 그냥 elements에 있는 요소들 넣는거니까 넣어줄 것
        if(len == 1){
            hashSet.add(elements[left++]);
            index += 1;
        }
        // elements[left] ~ elements[right] 까지의 합 
        else {
            
            console.log(elements[left++] + elements[(right++) % n]);
            // hashSet.add((elements[left++] + elements[(right++) % n]));
            index += 1;
        }
    }
    
    console.log(hashSet);
    return answer;
}