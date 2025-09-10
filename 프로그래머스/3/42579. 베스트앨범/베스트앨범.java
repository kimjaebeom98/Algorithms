import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        HashMap<String, Integer> genreTotal = new HashMap<>();
        HashMap<String, HashMap<Integer, Integer>> idxMap = new HashMap<>();
        for(int i=0; i<genres.length; i++){
            if(!genreTotal.containsKey(genres[i])){
                genreTotal.put(genres[i], plays[i]);
                HashMap<Integer, Integer> tmpMap = new HashMap<>();
                tmpMap.put(i, plays[i]);
                idxMap.put(genres[i], tmpMap);
            }else{
                genreTotal.put(genres[i], plays[i] + genreTotal.get(genres[i]));
                idxMap.get(genres[i]).put(i, plays[i]);
            }
        }
        
        List<String> keyList = new ArrayList(genreTotal.keySet());
        Collections.sort(keyList, (o1, o2) -> genreTotal.get(o2) - genreTotal.get(o1));
        
        for(String key : keyList){
            HashMap<Integer, Integer> tmpMap = idxMap.get(key);
            List<Integer> idxList = new ArrayList(tmpMap.keySet());
            Collections.sort(idxList, (o1, o2) -> tmpMap.get(o2) - tmpMap.get(o1));
            answer.add(idxList.get(0));
            if(idxList.size() >= 2)
                answer.add(idxList.get(1));
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}