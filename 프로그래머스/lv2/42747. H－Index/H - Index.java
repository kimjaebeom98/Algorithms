import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        // citations[i]번 이상 인용된 논문이 citations.length - i개 있다는 의미
        for(int i=0; i<citations.length; i++)
            if(citations[i] >= citations.length - i)
                return citations.length - i;
        return 0;
    }
}
