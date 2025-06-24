import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class App {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 5 3
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 5 4 3 2 1
        st = new StringTokenizer(br.readLine());
        int[] s = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            int tmp = Integer.parseInt(st.nextToken());
            s[i] = s[i - 1] + tmp;
        }

        // 1 3
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            System.out.println(s[end] - s[start - 1]);
        }

    }
}
