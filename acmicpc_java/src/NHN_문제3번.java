import java.io.IOException;
import java.util.Scanner;

public class NHN_문제3번 {
    private static int count = 0;
    private static boolean visited[];
    private static int[][] fight;

    private static void solution(int numOfConflict, int[][] conflicts) {
        fight = new int[9][9];

        // 싸우는 경우는 우선 모두 0이라 둠
        for (int i = 1; i <= 8; i++) {
            for (int j = 1; j <= 8; j++) {
                fight[i][j] = 0;
            }
        }

        // 갈등 관계인 경우는 싸울 가능성을 1로 두었음
        for (int i = 0; i < numOfConflict; i++) {
            fight[conflicts[i][0]][conflicts[i][1]] = fight[conflicts[i][1]][conflicts[i][0]] = 1;
        }
        visited = new boolean[9];
        for (int i = 1; i <= 8; i++) {
            dfs(i, 1, visited, fight, i);
        }
        System.out.println(count);
    }

    private static void dfs(int i, int size, boolean[] visited, int[][] fight, int total) {
        if (size == 8) {
            count += 1;
            return;
        }
        for (int j = 1; j <= 8; j++) {
            if (!visited[j]) {
                // 싸우지 않는 경우만 탐색돌기
                if (fight[i][j] == 0) {
                    // 포함관계 사절
                    if(!String.valueOf(total).contains(String.valueOf(j))){
                        visited[i] = true;
                        dfs(j, (size + 1), visited, fight, (10 * total) + j);
                        visited[i] = false;
                    }
                }
            }
        }
        //visited[i] = false;
    }

    private static class InputData {
        int numOfConflict;
        int[][] conflicts;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();
        try (Scanner scanner = new Scanner(System.in)) {
            inputData.numOfConflict = Integer.parseInt(scanner.nextLine());
            inputData.conflicts = new int[inputData.numOfConflict][2];
            for (int i = 0; i < inputData.numOfConflict; i++) {
                String[] temp = scanner.nextLine().split(" ");
                inputData.conflicts[i][0] = Integer.parseInt(temp[0]);
                inputData.conflicts[i][1] = Integer.parseInt(temp[1]);
            }
        } catch (Exception e) {
            throw e;
        }
        return inputData;
    }

    public static void main(String[] args) throws IOException {
        InputData inputData = processStdin();
        solution(inputData.numOfConflict, inputData.conflicts);
    }
}
