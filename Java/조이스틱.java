class Solution {
    public int solution(String name) {
        int answer = 0;
        int index = 0;
        int move_to_end_or_index = name.length() - 1; // 현재 i에서 index까지 간다는 것으로
        // 예를 들어, 처음 위치인 0부터 마지막까지 쭉 갔을때를 현 위치에서 최대치로 잡는 것입니다.
        // 최소값을 구할 때 보통 첫 비교값을 최대로 잡기 때문에 현재 위치 i에서 가장 많이 갈 수 있는건 끝까지 가는 것입니다.
        // 단, 끝까지 간 것과 정방향 이동, 역방향 이동을 각각 비교했을때 작은 값을 찾아서 값을 줄여가는 것이 핵심입니다.  
        // 정방향은 현재 위치에서 index까지 i만큼 이동한 것을 다시 현 위치로 와서 전체 길이 - index 만큼 다시 간 것을 말하며,
        // 역방향은 현 위치에서 (전체 - index)만큼 이동했다가 다시 처음 위치로 돌아와서 i만큼 이동한 
        for(int i=0;i<name.length();i++){
            int n1 = name.charAt(i) - 'A';
            int n2 = 'Z' - name.charAt(i) + 1;
            
            answer += Math.min(n1, n2); // 상하 체크하기
            index += 1; // 커서이동
            // A가 반복되는 경우 그냥 인덱스 이동시킬것
            while(index < name.length() && name.charAt(index) == 'A'){
                index += 1;
            }
            // 실제로 이동한 만큼의 거리를 비교해야함 (인덱스로 비교하면 생각한거와 다르게 진행될 것)  
            move_to_end_or_index = Math.min(move_to_end_or_index, i * 2 + name.length() - index);
            move_to_end_or_index = Math.min(move_to_end_or_index, (name.length()- index) * 2 + i);
            System.out.println("move_to_end_or_index: " + move_to_end_or_index + ", n1 : " + n1 +", n2 : "+ n2);
        }
        return answer + move_to_end_or_index;
    }
}