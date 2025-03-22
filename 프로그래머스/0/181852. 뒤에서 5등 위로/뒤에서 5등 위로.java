import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        List<Integer> list = new ArrayList<>();
        for(int num : num_list){
            list.add(num);
        }
        Collections.sort(list);
        
        int[] answer = new int[num_list.length-5];
        for(int i=0; i<num_list.length-5; i++)
            answer[i] = list.get(i+5);
        return answer;
    }
}