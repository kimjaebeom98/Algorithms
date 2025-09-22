import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times);
        long l = 0;
        long r = (long)times[times.length-1] * n;
        
        while(l <= r){
            // 해당 시간 동안 각 심사대별로 몇 명을 처리할 수 있는지 
            long mid = (l + r) / 2;
            long count = 0;
            for(int t : times){
                count += mid / t;
            }
            
            // 더 많은 사람들을 처리할 수 있음.
            if(count >= n){
                r = mid - 1;
                answer = mid;
            }else{
                l = mid + 1;
            }
            
        }
        
        return answer;
    }
}