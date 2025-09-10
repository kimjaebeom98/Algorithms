import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int count = 0;
        Deque<Integer[]> queue = new ArrayDeque<Integer[]>();
        for(int i=0; i<priorities.length; i++){
            Integer[] tmp = new Integer[2];
            tmp[0] = priorities[i];
            tmp[1] = i == location ? 1 : 0;
            queue.add(tmp);
        }
    
        while(!queue.isEmpty()){
            Integer[] tmp = queue.poll();
            
            boolean flag = true;
            for(Integer[] q : queue){
                if(q[0] > tmp[0]){
                    flag = false;
                    break;
                }
            }
            if(flag){
                count++;
                if(tmp[1] == 1)
                    return count;
            }
            else
                queue.add(tmp);
        }
        
        
        return count;
    }
}