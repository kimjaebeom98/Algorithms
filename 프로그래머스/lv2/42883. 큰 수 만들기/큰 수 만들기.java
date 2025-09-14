import java.util.*;

class Solution {
    public String solution(String number, int k) {
        // 결과를 담을 스택 (정확히는 덱DeQue가 더 유연하고 좋음)
        Deque<Character> stack = new ArrayDeque<>();
        
        for (char digit : number.toCharArray()) {
            // 스택이 비어있지 않고, 아직 k번 제거 기회가 남아있고,
            // 스택의 맨 위 숫자가 현재 숫자(digit)보다 작으면
            // (즉, 현재 숫자를 넣었을 때 더 큰 수를 만들 수 있다면)
            while (!stack.isEmpty() && k > 0 && stack.peekLast() < digit) {
                stack.removeLast(); // 스택 맨 위 숫자 제거
                k--; // 제거 기회 1회 사용
            }
            stack.addLast(digit); // 현재 숫자를 스택에 추가
        }

        // 만약 모든 숫자를 다 돌았는데도 k가 0이 아니면
        // (즉, 제거할 기회가 남아있다면)
        // 스택에 남은 숫자들 중 뒤쪽(작은 숫자)부터 k개만큼 제거한다.
        // ex) number="987", k=1 이면 위 로직에선 아무것도 제거 안 되고 [9,8,7]이 스택에 남음.
        //     이 경우, k=1이 남았으므로 7을 제거해야 함.
        while (k > 0) {
            stack.removeLast();
            k--;
        }

        // 스택에 담긴 숫자들을 문자열로 변환한다.
        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }
        
        // 최종 결과 문자열 반환
        return sb.toString();
    }
}
