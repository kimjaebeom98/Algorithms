import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {}; // 초기화는 좋은데, 사실상 사용 안 함 (아래에서 바로 return하니까)
        int colorSum = brown + yellow; // 전체 격자 수

        // HashSet<int[]> set = new HashSet<>(); // <- 여기서 문제!
        // int[]는 참조 타입이라 hashCode()와 equals()가 오버라이딩 안 되어 있으면
        // 값이 같아도 다른 객체로 인식해서 중복 제거가 안 됨.
        // 예를 들어 new int[]{1, 2} 와 new int[]{1, 2}는 다른 객체로 처리됨.
        // 그리고 굳이 Set에 저장할 필요 없이 바로 조건을 체크하면 됨.

        int chkMaxNum = (int)Math.sqrt(colorSum);
        for(int i=1; i<=chkMaxNum; i++){
            if(colorSum % i == 0){ // i가 약수라면
                int width = colorSum / i; // 가로 길이 (큰 값)
                int height = i;           // 세로 길이 (작은 값)

                // (가로-2) * (세로-2)가 yellow 격자 수와 같은지 확인
                // 그리고 가로는 세로보다 길거나 같아야 함 (문제 조건)
                if (width >= height && (width - 2) * (height - 2) == yellow) {
                    // 테두리 갈색 격자 수를 확인하는 로직 (brown = 전체 - yellow)
                    // 네 코드는 ((tmp[1] - 2) * 2) + (tmp[0] * 2) == brown 이었네?
                    // 이건 테두리의 가로 세로를 각각 2줄로 가정하고 계산하는 방식인데,
                    // 이건 테두리 부분이 1줄이라는 문제 정의랑 안 맞을 수도 있어!
                    // 정확한 brown 격자 수는 (가로 * 세로) - yellow = brown 이잖아.
                    // (width * height - yellow) == brown 이거나
                    // 2 * (width + height) - 4 = brown (가장자리 중복 제거)
                    // 이런 식으로 해야 하는데, 어차피 (width * height) == colorSum이니까
                    // (colorSum - yellow) == brown 은 늘 참이고, 이 조건은 생략 가능!
                    // 핵심은 (width - 2) * (height - 2) == yellow 요 조건이지!
                    return new int[]{width, height}; // 찾으면 바로 반환!
                }
            }
        }
        return new int[]{}; // 이 코드가 실행될 일은 없을 거야 (문제는 항상 답이 있다고 가정하므로)
    }
}
