import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] dueDates = new int[progresses.length];
        
        for(int i=0; i<dueDates.length; i++)
            dueDates[i] = (100 - progresses[i]) % speeds[i] > 0 ? (100 - progresses[i]) / speeds[i] + 1 : (100 - progresses[i]) / speeds[i];    
        
        Deque<Integer> queue = new ArrayDeque<>();
        for(int i=0; i<dueDates.length; i++)
            queue.addLast(dueDates[i]);
        
        int count = 0;
        int tmp = 0;
        Deque<Integer> result = new ArrayDeque<>();
        
        while(!queue.isEmpty()){
            if(count == 0){
                tmp = queue.pollFirst();
                count++;
                continue;
            } 
            
            if(tmp >= queue.peekFirst()){
                queue.pollFirst();
                count++;
            }else{
                result.addLast(count);
                count = 0;
            } 
        }
        
        if(count != 0)
            result.addLast(count);
        
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}