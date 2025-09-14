import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length; // 행의 길이
        int m = maps[0].length; // 열의 길이
    
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        int[][] distance = new int[n][m]; // 현재(x, y) 지점의 최단 거리를 저장
        Queue<int[]> q = new LinkedList<>();
        
        // 동, 서, 남, 북
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        q.offer(new int[]{0,0});
        visited[0][0] = true;
        distance[0][0] = 1;
        
        while(!q.isEmpty()){
            int[] curPos = q.poll();
            int curX = curPos[0];
            int curY = curPos[1];
            
            if(curX == n-1 && curY == m-1)
                return distance[curX][curY];
            
            for(int i=0; i<4; i++){
                // 이동 시켰을 때
                int nx = curX + dx[i];
                int ny = curY + dy[i];
                
                // 이동 가능하다면
                if(nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && maps[nx][ny] == 1){
                    visited[nx][ny] = true;
                    distance[nx][ny] = distance[curX][curY] + 1;
                    q.offer(new int[]{nx, ny});
                }
            }
            
        }
        
        // q에서 탐색을 못 한 경우 = 상대 팀 진영에 도착할 수 없을 때
        return -1;
    }
}
