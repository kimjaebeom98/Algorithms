/*
재귀함수를 이용해서 풀 수 있을 듯?
재귀함수(숫자들, 현재값 - 다음값, 타겟값, 깊이)
return 조건 : depth가 numbers.length와 같으면 -> target값과 같은지 검증
*/

class Solution {
    
    int count = 0;
    
    void recursive(int[] numbers, int curNum, int target, int depth){
        if(depth == numbers.length){
            if(target == curNum)
                count++;
            return;
        }
        
        recursive(numbers, curNum - numbers[depth], target, depth+1);
        recursive(numbers, curNum + numbers[depth], target, depth+1);
        
    }
    
    
    public int solution(int[] numbers, int target) {
        recursive(numbers, 0, target, 0);
        return count;
    }
}
