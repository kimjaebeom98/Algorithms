import java.io.BufferedReader;
import java.io.InputStreamReader;

public class App {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split("");
        int[] nums = new int[input.length];

        for (int i = 0; i < nums.length; i++)
            nums[i] = Integer.parseInt(input[i]);

        for (int idx = 0; idx < nums.length; idx++) {
            int maxIdx = idx;
            for (int j = idx + 1; j < nums.length; j++) {
                if (nums[maxIdx] < nums[j])
                    maxIdx = j;
            }
            if (nums[idx] < nums[maxIdx]) {
                int tmp = nums[idx];
                nums[idx] = nums[maxIdx];
                nums[maxIdx] = tmp;
            }
        }
        String result = "";
        for (int i = 0; i < nums.length; i++) {
            result += nums[i];
        }
        System.out.println(result);

    }
}
