import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        List<String> resList = new ArrayList<>();
        for(int number : numbers)
            resList.add(Integer.toString(number));
        // (s2 + s1).compareTo(s1 + s2) = (s2 + s1) - (s1 + s2)
        // s1 = "3", s2 = "30" 이라고 가정했을 때
        // "303".compareTo("330") = "303" - "330"(아스키코드값) = (-) 
        // compare(A, B)의 결과가 음수(-)면 A가 B보다 작다고 생각하고 A를 B앞에 배치(기본 오름차순이니깐)
        // 따라서 "3" 그다음 "30"이 옴 
        // s1 = "30", s2 = "3"이면 양수(+)가 나올거고 A가 B보다 크다고 생각하고 A를 B뒤에 배치
        // Collections.sort가 정렬을 할 때, 리스트 안의 모든 요소들을 가져다가 '둘씩 짝 지어서' 어떤 게 앞에 와야 할지 계속 물어보고 그에 따라 순서를 바꿈
        Collections.sort(resList, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));
        
        if("0".equals(resList.get(0)))
            return "0";
        
        for(String s : resList)
            answer += s;
        
        
        return answer;
    }
}
