import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class App {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // n : nxn 배열
        // m : 질의
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] arr = new int[n + 1][n + 1];
        for (int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j < n + 1; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        /*
         * for (int i = 1; i < n + 1; i++) {
         * for (int j = 1; j < n + 1; j++) {
         * System.out.print(Integer.toString(arr[i][j]) + ' ');
         * }
         * System.out.println();
         * }
         */
        int[][] sumArr = new int[n + 1][n + 1];
        // 초기값 선언
        sumArr[1][1] = arr[1][1];
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (i == 1 && j == 1)
                    continue;

                sumArr[i][j] = sumArr[i - 1][j] + sumArr[i][j - 1] - sumArr[i - 1][j - 1] + arr[i][j];
            }
        }
        /*
         * for (int i = 1; i < n + 1; i++) {
         * for (int j = 1; j < n + 1; j++) {
         * System.out.print(Integer.toString(sumArr[i][j]) + ' ');
         * }
         * System.out.println();
         * }
         */
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            System.out.println(sumArr[x2][y2] - sumArr[x1 - 1][y2] - sumArr[x2][y1 - 1] + sumArr[x1 - 1][y1 - 1]);
        }

    }
}
