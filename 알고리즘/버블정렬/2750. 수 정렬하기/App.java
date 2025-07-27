import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        // 입력받고자 하는 수의 개수 N
        int N = sc.nextInt();
        // 입력받은 수를 저장하는 배열 선언
        int[] nums = new int[N];

        for (int i = 0; i < N; i++)
            nums[i] = sc.nextInt();

        // N개의 배열의 값을 탐색
        for (int idx = 0; idx < nums.length; idx++) {
            // 순서대로 제일 큰 값을 맨 뒤로 보낼 예정이므로 정렬된 범위는 더이상 탐색 x
            for (int j = 0; j < N - 1 - idx; j++) {
                if (nums[j] > nums[j + 1]) {
                    int tmp = nums[j + 1];
                    nums[j + 1] = nums[j];
                    nums[j] = tmp;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            System.out.println(nums[i]);
        }
    }
}
