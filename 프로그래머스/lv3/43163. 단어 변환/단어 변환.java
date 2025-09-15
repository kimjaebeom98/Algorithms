import java.util.*;

class Solution {
    
    boolean[] visited;
    int count = 51;
    
    void recursive(String curWord, String target, int depth, String[] words){
        if(curWord.equals(target)){
            count = Math.min(count, depth);
            return;
        }
            
        depth++;
        
        if(depth == words.length)
            return;
        
        String[] curWordList = curWord.split("");
        for(int j=0; j<words.length; j++){
            String[] wordList = words[j].split("");
            int cnt = 0;
            for(int i=0; i<wordList.length; i++){
                if(!curWordList[i].equals(wordList[i]))
                    cnt++;
            }
            if(cnt == 1 && !visited[j]){
                visited[j] = true;
                recursive(words[j], target, depth, words);
                visited[j] = false;
            }
            
        }
        
    }
    
    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
        recursive(begin, target, 0, words);
        return count < 51 ? count : 0;
    }
}
