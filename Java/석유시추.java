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
                    int size = move(i, j, landId); // 이동한 땅의 주인은 지속해서 확장 가능한 땅일 경우 본인 소유가 될 것 (시추관 위치)
                    landOperator.put(landId, size);
                    landId += 1;
                }
            }
        }
        int[] colOil = new int[n2];
        // 열 내리면서 행 체크 -> 각 열마다의 석유량을 더해줘야함
        for(int j=0;j<n2;j++){
            Set<Integer> oilSet = new HashSet<>();  
            // 각 땅에 대해서는 landId가 입력되어 있을것이고, 석유가 흐르는 곳이기에 
            // 다음 조건을 넣어두었고 각 땅마다 아이디 값이 있을테니 중복을 제거하기 위해서 Set을 정의합니다. 
            for(int i=0;i<n1;i++){
                if(land[i][j] == 1){
                    oilSet.add(oilMap[i][j]);
                }
            }
            // Set에 landId값이 중복되지 않은채로 잘 들어가게 된다면, 해당 landId값으로 저장된 값들(Size) 가져와서 열의 석유량합에 더해줍니다.
            for(int id : oilSet){
                colOil[j] += landOperator.get(id);
            }
        }
        // 가장 많은 석유량이 답입니다.
        int count = Arrays.stream(colOil).max().getAsInt();  ;
        
        return count;
    }
    
    public int move(int row, int col, int landId){
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
                    size++;
                }
            }
        }
        
        return size;
    }
}