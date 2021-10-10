import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class ACM호텔 {
    private static int testCase;
    private static int height;
    private static int roomCnt;
    private static int passengerCnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        testCase = Integer.parseInt(st.nextToken());

        for (int i = 0; i < testCase; i++) {
            int answer = 0;
            st = new StringTokenizer(br.readLine());
            height = Integer.parseInt(st.nextToken());
            roomCnt = Integer.parseInt(st.nextToken());
            passengerCnt = Integer.parseInt(st.nextToken());
            answer = acmHotelRoomNumber(height, roomCnt, passengerCnt);
            System.out.println(answer);
        }
    }

    private static int acmHotelRoomNumber(int h, int w, int n) {
        int res = 0;
        int hotelStair = 0;
        int hotelRoomNumber = 0;
        hotelStair = n % h;
        if (hotelStair == 0) {
            hotelStair = h * 100;
            hotelRoomNumber = (n / h);
        } else {
            hotelStair = hotelStair * 100;
            hotelRoomNumber = (n / h) + 1;
        }

        res = hotelStair + hotelRoomNumber;
        return res;
    }
}
