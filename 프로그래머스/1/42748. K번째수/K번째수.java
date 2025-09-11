import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int i=0; i<commands.length; i++){
            int startIdx = commands[i][0];
            int endIdx = commands[i][1];
            int targetIdx = commands[i][2];
            int[] tmpArray = new int[endIdx - startIdx + 1];
            int tmpIdx = 0;
            for(int j=startIdx-1; j<endIdx; j++){
                tmpArray[tmpIdx++] = array[j];
            }
            Arrays.sort(tmpArray);
            answer[i] = tmpArray[targetIdx-1];
                
        }
        return answer;
    }
}