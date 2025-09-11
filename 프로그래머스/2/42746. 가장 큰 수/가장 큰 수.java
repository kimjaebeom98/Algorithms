import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        List<String> resList = new ArrayList<>();
        for(int number : numbers)
            resList.add(Integer.toString(number));
        
        Collections.sort(resList, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));
        
        if("0".equals(resList.get(0)))
            return "0";
        
        for(String s : resList)
            answer += s;
        
        
        return answer;
    }
}