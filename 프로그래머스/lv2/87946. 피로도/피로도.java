/*
던전의 길이가 1이상 8이하인 것으로 보아 조합으로 해도 될 듯? -> 재귀
1. 모든 던전의 조합을 탐험한다. -> DFS, 재귀
    1-1. (현재 피로도, 다음 탐험할 던전들)을 인수로 가진 함수를 만든다.
    1-2. 남은 던전 중 하나를 탐험 할 수 있으면 현재 던전을 방문했다는 표시 후 재귀
    1-3. 재귀에서 빠져나오면 방문했다는 표시를 삭제
*/
class Solution {
    boolean[] visited;
    int count = 0;
    // curK : 현재 피로도, dungeons : 탐험 할 던전 들, depth : 탐험한 던전의 갯수
    public void recursive(int curK, int[][] dungeons, int depth){
        for(int i=0; i<dungeons.length; i++){
            // 탐험할 수 있으면
            if(curK >= dungeons[i][0] && !visited[i]){
                // 방문 표시
                visited[i] = true;
                // 현재 피로도 - 소모 피로도, 던전, 탐험 갯수 + 1 
                recursive(curK - dungeons[i][1], dungeons, depth+1);
                // 방문 완료
                visited[i] = false;
            }
        }
        // 최대 방문까지 왔을 때, 값 비교
        count = Math.max(count, depth);
    }
    
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        recursive(k, dungeons, 0);
        return count;
    }
}
