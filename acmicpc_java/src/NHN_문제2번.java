import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class NHN_문제2번 {
    private static Integer[] attack;

    private static void solution(int numOfRegion, int numOfAttackableFrequency, int[][] frequencies) {
        attack = new Integer[21]; // 주파수는 20 이하의 자연수
        for (int i = 0; i < attack.length; i++)
            attack[i] = 0;

        for (int i = 0; i < numOfRegion; i++) {
            for (int j = 0; j < frequencies[i].length; j++) {
                attack[frequencies[i][j]] += 1;
            }
        }
        Arrays.sort(attack, Collections.reverseOrder());
        int answer = 0;
        for (int i = 0; i < numOfAttackableFrequency; i++) {
            answer += attack[i];
        }
        System.out.print(answer);
    }

    private static class InputData {
        int numOfRegion;
        int numOfAtackableFrequency;
        int[][] frequencies;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();
        try (Scanner scanner = new Scanner(System.in)) {
            String[] temp = scanner.nextLine().split(" ");
            inputData.numOfRegion = Integer.parseInt(temp[0]);
            inputData.numOfAtackableFrequency = Integer.parseInt(temp[1]);
            inputData.frequencies = new int[inputData.numOfRegion][];

            for (int i = 0; i < inputData.numOfRegion; i++) {
                temp = scanner.nextLine().split(" ");
                int numOfFrequency = Integer.valueOf(temp[0]);
                inputData.frequencies[i] = new int[numOfFrequency];
                for (int j = 0; j < numOfFrequency; j++) {
                    inputData.frequencies[i][j] = Integer.parseInt(temp[j + 1]);
                }
            }
        } catch (Exception e) {
            throw e;
        }
        return inputData;
    }

    public static void main(String[] args) throws IOException {
        InputData inputData = processStdin();
        solution(inputData.numOfRegion, inputData.numOfAtackableFrequency, inputData.frequencies);
    }
}
