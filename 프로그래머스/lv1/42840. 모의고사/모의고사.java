import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] score = new int[3];
        List<Integer> answer = new ArrayList<>();
        int[][] patterns = {{1, 2, 3, 4, 5}, {2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        
        for(int i=0; i<score.length; i++){
            int count = 0;
            for(int j=0; j<answers.length; j++){
                if(answers[j] == patterns[i][j % patterns[i].length])
                    count++;
            }
            score[i] = count;
        }
        
        int maxCount = Math.max(score[0], Math.max(score[1], score[2]));
        
        for(int i=0; i<score.length; i++){
            if(maxCount == score[i])
                answer.add(i+1);
        }
        
        return answer.stream().mapToInt(value -> value).toArray();
    }
}
