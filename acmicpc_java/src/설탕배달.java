import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 설탕배달 {
    private static int totalCnt = Integer.MAX_VALUE;
    private static int input;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        input = Integer.parseInt(st.nextToken());
        int sepCnt = (input / 5);
        if(input == 1 || input == 2 || input == 4 || input == 7) {
            System.out.println(-1);
            return;
        }
        for (int i = sepCnt; i >= 0; i--) {
            totalCnt = Math.min(totalCnt, sepFiveFunc((5 * i), (input - (5 * i)), i));
        }
        System.out.println(totalCnt);
    }

    private static int sepFiveFunc(int N, int rest, int cnt) {
        if (N == input) {
            // 5로 한번에 나눠진 케이스
            return cnt;
        }
        if(sepThreeFunc(rest) == 0)
            return Integer.MAX_VALUE;
        return cnt + sepThreeFunc(rest);
    }

    private static int sepThreeFunc(int N) {
        int rest = N % 3;
        int cnt = 0;
        if (rest == 0) {
            for (int i = 0; i < (N / 3); i++) {
                cnt += 1;
            }
            return cnt;
        } else {
            // 3으로 나눠지지 않은 경우
            return 0;
        }
    }
}
