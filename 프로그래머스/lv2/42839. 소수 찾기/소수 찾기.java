import java.util.*;
// 숫자의 조합을 저장
// 소수 인지 파악한다(0과 1은 소수가 아니다)
class Solution {
    HashSet<Integer> combSet = new HashSet<>(); // 숫자의 조합을 담을 세트 
    public int solution(String numbers) {
        int answer = 0;
        // 1. 숫자의 조합을 저장
        // 처음에는 조합이 없으므로 빈 스트링, 다른 숫자들에서 조합을 찾아야 하므로 전체
        makeNumComb("", numbers);
        
        for(Integer comb : combSet){
            if(isPrime(comb))
                answer++;
        }
        
        return answer;
    }
    
    public void makeNumComb(String comb, String others){
        if(!"".equals(comb))
            combSet.add(Integer.parseInt(comb));
        
        for(int i=0; i<others.length(); i++){
            makeNumComb(comb + others.charAt(i), others.substring(0, i) + others.substring(i+1));
        }
    }
    
    public boolean isPrime(int num){
        if(num == 0 || num == 1)
            return false;
        
        // 에라토스테네스의 체
        int maxChkNum = (int)Math.sqrt(num);
        for(int i=2; i<=maxChkNum; i++){
            if(num % i == 0)
                return false;
        }
        
        return true;
    }
            

    
}
