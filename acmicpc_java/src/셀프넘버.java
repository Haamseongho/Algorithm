import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class 셀프넘버 {
    private static ArrayList<Integer> notSelfNumberList;
    private static ArrayList<Integer> selfNumberList;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        notSelfNumberList = new ArrayList<>();
        selfNumberList = new ArrayList<>();
        for (int i = 1; i <= 10000; i++)
            selfNumber(i);

        for (int i = 1; i <= 10000; i++) {
            if (!notSelfNumberList.contains(i)) {
                System.out.println(i);
            }
        }
    }

    private static void selfNumber(int n) {
        int res = 0;
        String str = String.valueOf(n);
        for (int i = 0; i < str.length(); i++) {
            res = res + Integer.parseInt(String.valueOf(str.charAt(i)));
        }
        int ans = n + res;
        notSelfNumberList.add(ans);
        // selfNumber(n + 1);
    }
}
