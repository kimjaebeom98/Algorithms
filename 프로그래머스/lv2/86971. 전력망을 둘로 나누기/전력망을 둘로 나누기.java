import java.util.*;
class Solution {
    public int solution(int n, int[][] wires) {
        int answer = n;
        List<Integer>[] graph = new List[n+1];
        
        for(int i=0; i<n+1; i++){
            graph[i] = new ArrayList<>();
        }
        
        for(int i=0; i<wires.length; i++){
            graph[wires[i][0]].add(wires[i][1]);
            graph[wires[i][1]].add(wires[i][0]); 
        }
        
        for(int i=0; i<wires.length; i++){
            int start = wires[i][0];
            int preVisited = wires[i][1];
            
            boolean[] visited = new boolean[n+1];
            // 이미 방문 처리해서 전력망을 자르는 효과
            visited[preVisited] = true;
            
            Queue<Integer> q = new LinkedList<Integer>();
            q.offer(start);
            visited[start] = true;
            int cnt = 1;
            while(!q.isEmpty()){
                int cur = q.poll();
                
                for(Integer num : graph[cur]){
                    if(!visited[num]){
                        visited[num] = true;
                        q.add(num);
                        cnt++;
                    }
                }
                
            }
            int tmp;
            if(n-cnt < cnt)
                tmp = cnt - (n-cnt);
            else
                tmp = (n-cnt) - cnt;
            
            answer = Math.min(answer, tmp);
                
            
            
            
        }
        return answer;
    }
}
