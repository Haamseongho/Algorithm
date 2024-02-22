import java.util.*;
class Solution {
    boolean[][] visited;
    int[][] land;
    int n1, n2;
    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, -1, 0, 1};
    int[][] oilMap;
    HashMap<Integer, Integer> landOperator;
    int[] landMap;
    public int solution(int[][] land) {
        this.land = land;
        this.n1 = land.length; // 행 
        this.n2 = land[0].length; // 열 
        this.visited =  new boolean[n1][n2];
        oilMap = new int[n1][n2]; // 시추관이 차지한 땅
        this.landOperator = new HashMap<>(); // landId가 차지한 땅의 갯수 (landId = Key, 차지한 땅의 갯수 = Value)
        this.landMap = new int[n2];
        int landId = 1;
        // 열로 먼저 검증 
        for(int i=0;i<n1;i++){
            for(int j=0;j<n2;j++){
                if(!visited[i][j] && land[i][j] == 1){
                    move(i, j, landId); // 이동한 땅의 주인은 지속해서 확장 가능한 땅일 경우 본인 소유가 될 것 (시추관 위치)
                    landId += 1;
                }
            }
        }
        
        for(int i=0;i<n2;i++){
            int count = 0;
            int sichu = 0;
            for(int j=0;j<n1;j++){
                if(!map.contains(oilMap[i][j])){
                    count += map.get(oilMap[i][j]);
                    map.put()
                }
                count = Math.max(count, map.get(oilMap[i][j]));
            }
        }
        return count;
    }
    
    public void move(int row, int col, int landId){
        // 동서남북 이동 배열
    
        Queue<int []> queue = new LinkedList<>();
        queue.offer(new int[]{row, col});
        visited[row][col] = true;
        oilMap[row][col] = landId; // 시추관 번호를 땅에 입력해줌(해당 땅은 시추관 것)
        int size = 1;
        while(!queue.isEmpty()){
            int[] currentXY = queue.poll();
            int mx = 0;
            int my = 0;
            for(int i=0;i<4;i++){
                mx = currentXY[0] + dx[i];
                my = currentXY[1] + dy[i];
                // 범위내에 있는지 확인
               
                if((mx >= 0 && mx < n1) && (my >= 0 && my < n2) && (!visited[mx][my]) && (land[mx][my] == 1)){
                    queue.offer(new int[]{mx, my});
                    visited[mx][my] = true;
                    oilMap[mx][my] = landId; // 이동해서도 해당 시추관 번호를 입력해줄것
                    // System.out.println("x : " + mx +", y : " + my +", size : " + size);
                    size += 1;
                }
            }
        }
    }
}