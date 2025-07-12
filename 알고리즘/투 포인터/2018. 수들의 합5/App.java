import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] s = new int[n + 1];
        s[1] = 1;
        for (int i = 2; i < n + 1; i++)
            s[i] = s[i - 1] + i;

        // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

        int count = 0;
        int start = 1;
        int end = 1;
        while (end <= n) {
            if (s[end] - s[start - 1] < n)
                end += 1;
            else if (s[end] - s[start - 1] == n) {
                count += 1;
                start += 1;
                end += 1;
            } else
                start += 1;

        }

        System.out.println("count : " + Integer.toString(count));
    }

}
