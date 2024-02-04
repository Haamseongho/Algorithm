class Solution {
    public int solution(int[][] triangle) {
        int dp[][] = new int[triangle.length][triangle.length];
        dp[0][0] = triangle[0][0]; // 처음 값은 넣어주기 
        /*
            dp[1][0] -> dp[0][0]
            dp[0][1] -> dp[0][0]
            dp[2][0] -> dp[1][0] 
            dp[2][1] -> dp[1][0], dp[1][1] 중 더 큰 것으로 (dp[1][0]은 dp[0][0]을 합한 값, dp[1][1]은 dp[0][0]을 합한 값)
        */
        for(int i=1;i<triangle.length;i++){
            for(int j=0;j<triangle[i].length;j++){
                // 오른쪽 가장 바깥라인에 잡히는 구조 
                if(i == j){
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1];
                } 
                // 가장 왼쪽 바깥라인에 잡히는 구조
                else if(j == 0){
                    dp[i][j] = triangle[i][j] + dp[i-1][j];
                } 
                // 그 외 안쪽에 잡히는 구조로 이 전 합계 dp값과 비교
                else {
                    dp[i][j] = (dp[i-1][j-1] > dp[i-1][j] ? dp[i-1][j-1] : dp[i-1][j]) + triangle[i][j];
                }
            }   
        }
        // 마지막 행까지 갔을때 열 다 비교하면서 최고값 뽑아내기
        int answer = 0;
        for(int i=0;i<triangle.length;i++){
            answer = Math.max(dp[triangle.length-1][i], answer);
        }
        return answer;
    }
}