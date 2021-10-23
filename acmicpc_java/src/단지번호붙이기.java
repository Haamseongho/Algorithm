import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class 단지번호붙이기 {
    private static int count = 0;
    private static int dx[] = {-1, 0, 1, 0};
    private static int dy[] = {0, 1, 0, -1};
    private static int size = 0;
    private static ArrayList<Integer> countList;
    private static boolean visited[][];

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        size = sc.nextInt();
        int maze[][] = new int[size][size];
        visited = new boolean[size][size];
        countList = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            String str = sc.next();
            for (int j = 0; j < size; j++) {
                maze[i][j] = (int) (str.charAt(j) - 48);
                visited[i][j] = false;
            }
        }

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (maze[i][j] == 1) {
                    count = 0;
                    if (!visited[i][j]) { // 방문하지 않은곳에서 dfs 시작
                        dfs(maze, i, j);
                        countList.add(count);
                    }
                }
            }
        }
        System.out.println(countList.size());
        Collections.sort(countList);
        for (int i = 0; i < countList.size(); i++)
            System.out.println(countList.get(i));
    }

    private static void dfs(int[][] maze, int x, int y) {
        if ((x < 0) || (x >= size) || (y < 0) || (y >= size)) {
            return;
        }
        if (maze[x][y] == 0) {
            return;
        }
        visited[x][y] = true; // 현재 위치는 방문완료
        count += 1; // 이동횟수 체크
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < size && ny >= 0 && ny < size) {
                if (!visited[nx][ny]) {
                    dfs(maze, nx, ny);
                }
            }
        }
    }
}
