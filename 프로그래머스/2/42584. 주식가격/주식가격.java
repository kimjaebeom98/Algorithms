import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        List<Integer> resList = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        for(int price : prices)
            q.offer(price);
        
        while(!q.isEmpty()){
            int count = 0;
            int tmpPrice = q.poll();
            for(Integer price : q ){
                count++;
                if(tmpPrice > price)
                    break;
            }
            resList.add(count);
        }
        
        return resList.stream().mapToInt(Integer::intValue).toArray();
    }
}