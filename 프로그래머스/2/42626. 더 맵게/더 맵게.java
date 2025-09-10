import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pQ = new PriorityQueue<Integer>();
        for(int sc : scoville)
            pQ.offer(sc);
        
        while(K > pQ.peek()){
            if(pQ.size() < 2){
                break;
            }
            int newScoville = pQ.poll() + pQ.poll() * 2;
            answer++;
            pQ.offer(newScoville);
        }
        
        if(pQ.size() < 2 && K > pQ.peek())
            return -1;
        
        return answer;
    }
}