import java.io.IOException;
import java.util.*;

public class NHN_문제1번 {
    private static ArrayList<Integer> branchList;
    private static ArrayList<Integer> mergeList;

    private static void solution(int numOfOperation, Operation[] operations) {
        branchList = new ArrayList<>();
        mergeList = new ArrayList<>();
        int branchNumber = 2;
        branchList.add(1);
        for (int i = 0; i < numOfOperation; i++) {
            if (operations[i].type.toString().equals("branch")) {
                if (mergeList.size() == 0) {
                    branchList.add(branchNumber);
                    branchNumber += 1;
                } else {
                    Collections.sort(mergeList);
                    branchList.add(mergeList.get(0));
                    mergeList.remove(0);
                }
            } else {
                System.out.println("op:" + operations[i].value);
                mergeList.add(operations[i].value);
                branchList.remove(branchList.indexOf(operations[i].value));
            }
        }
        Collections.sort(branchList);
        for (int i = 0; i < branchList.size(); i++) {
            System.out.print(branchList.get(i) + " ");
        }
    }

    private static class InputData {
        int numOfOperation;
        Operation[] operations;
    }

    private static class Operation {
        OperationType type;
        Integer value;

        public Operation(OperationType type, Integer value) {
            this.type = type;
            this.value = value;
        }
    }

    private static enum OperationType {
        branch,
        merge;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();
        try (Scanner scanner = new Scanner(System.in)) {
            inputData.numOfOperation = Integer.parseInt(scanner.nextLine());
            inputData.operations = new Operation[inputData.numOfOperation];
            for (int i = 0; i < inputData.numOfOperation; i++) {
                String[] temp = scanner.nextLine().split(" ");
                Integer value = null;
                OperationType operationType = OperationType.valueOf(temp[0]);
                if (OperationType.merge == operationType) {
                    value = Integer.valueOf(temp[1]);
                }

                inputData.operations[i] = new Operation(operationType, value);
            }
        } catch (Exception e) {
            throw e;

        }
        return inputData;
    }

    public static void main(String[] args) throws IOException {
        InputData inputData = processStdin();
        solution(inputData.numOfOperation, inputData.operations);
    }
}
