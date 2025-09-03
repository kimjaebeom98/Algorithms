import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        String[] arrayS = s.split("");
        int count = 0;
        for(int i=0; i<arrayS.length; i++){
            if("(".equals(arrayS[i]))
                count += 1;
            else{
                count -= 1;
                if(count < 0)
                    return false;
            }
        }
        
        if(count != 0)
            return false;
        

        return answer;
    }
}