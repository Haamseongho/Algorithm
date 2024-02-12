class Solution {
    public int solution(String name) {
      
        int answer = 0;
        int index = 0;
        for(int i=0;i<name.length();i++){
            int n1 = name.charAt(i) - 65;
            int n2 = 90 - name.charAt(i);
            index += 1; // 커서이동
            // A가 반복되는 경우 그냥 인덱스 이동시킬것
            while(index < name.length() && name.charAt(index) == 'A'){
                index += 1;
            }
            
            answer += Math.min(n1, n2) + index;
        }
        return answer;
    }
}