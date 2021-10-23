import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 숨바꼭질 {
    private static int count = 0; // 이동횟수
    private static int minCount = Integer.MAX_VALUE;
    private static int N, M;
    private static Queue<MoveNode> queueList;
    private static boolean visited[];


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt(); // 수빈이 위치
        M = sc.nextInt(); // 동생 위치
        queueList = new LinkedList<>();
        visited = new boolean[100001];
        queueList.add(new MoveNode(N, 0));
        visited[N] = true;
        move(N);
        System.out.print(minCount);
    }

    private static boolean isMove(int N) {
        if (N < 0 || N > 100000 || visited[N])
            return false;
        return true;
    }

    // N이 이동
    private static void move(int N) {
        while (!queueList.isEmpty()) {
            int data = queueList.peek().node;
            int depth = queueList.poll().depth;
            if (data == M) {
                minCount = Math.min(minCount, depth);
                break;
            } else {
                if (isMove(data - 1)) {
                    visited[data - 1] = true;
                    queueList.add(new MoveNode(data- 1, depth + 1));
                }
                if (isMove(data + 1)) {
                    visited[data + 1] = true;
                    queueList.add(new MoveNode(data + 1, depth + 1));
                }
                if (isMove(data * 2)) {
                    visited[data * 2] = true;
                    queueList.add(new MoveNode(data * 2, depth + 1));
                }
            }
        }
    }

    private static class MoveNode {
        int node, depth;

        MoveNode(int N, int D) {
            this.node = N;
            this.depth = D;
        }
    }
}

