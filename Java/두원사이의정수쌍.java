class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;
        for(int i=1;i<=r2;i++){
            int minY = (int)Math.ceil(Math.sqrt(1.0 * r1 * r1 - 1.0 * i * i));
            int maxY = (int)Math.floor(Math.sqrt(1.0 * r2 * r2 - 1.0 * i * i));
            // System.out.println("minY : " +minY +", maxY : " + maxY);
            answer += (maxY - minY) + 1;
        }
        
        answer *= 4;
        return answer;
    }
}