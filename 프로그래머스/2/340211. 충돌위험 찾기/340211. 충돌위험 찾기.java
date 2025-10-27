import java.util.*;

class Solution {
    
    public static class Pos{
        public int y, x;
        
        public Pos(int y, int x){
            this.y = y;
            this.x = x;
        }
    }
    
    public static class Robot{
        public Pos pos;
        public List<Pos> posList;
        
        public Robot(Pos pos){
            this.pos = pos;
            posList = new ArrayList<>();
        }
        
        public boolean movePos(int[][] intArray){
            // 목표지점에 도달했으면 제거
            if(posList.size() > 0 && posList.get(0).y == pos.y && posList.get(0).x == pos.x){
                posList.remove(0);
            }
            
            // 로봇이 현재 위치를 벗어날 예정이니 1 감소
            intArray[pos.y][pos.x]--;
            
            // 도달했으면
            if(posList.size() == 0){
                return false;
            }
            
            // 목표 지점을 향해 다음으로 이동
            if(posList.get(0).y != pos.y){
                if(posList.get(0).y > pos.y)
                    pos.y++;
                else
                    pos.y--;
            }else if(posList.get(0).x != pos.x){
                if(posList.get(0).x > pos.x)
                    pos.x++;
                else
                    pos.x--;
            }
            // 이동한 로봇의 위치 업데이트
            intArray[pos.y][pos.x]++;
            
            return true;
        }
        
    }
    
    
    public int solution(int[][] points, int[][] routes) {
        int answer = 0;
        int[][] intArray = new int[101][101];
        
        List<Robot> list = new ArrayList<>();
        for(int i=0; i<routes.length; i++){
            int[] source = points[routes[i][0] - 1];
            int[] target = points[routes[i][1] - 1];
            
            Pos pos = new Pos(source[0], source[1]);
            // 현재 robot의 위치로 초기화 및, 목표 위치 저장
            Robot robot = new Robot(pos);
            intArray[pos.y][pos.x]++;
            
            // 로봇의 이동 경로 (시작점 이후 모든 지점)를 posList에 추가
            for (int j = 1; j < routes[i].length; j++) {
                int targetPointIndex = routes[i][j] - 1;
                robot.posList.add(new Pos(points[targetPointIndex][0], points[targetPointIndex][1]));
            }
            list.add(robot);
            
        }
        
        // 초반부터 충돌지점이 있는 지 체크
        for(int[] tmp : intArray){
            for(int val : tmp){
                if(val > 1){
                    answer++;
                }
            }
        }
        
        while(list.size() > 1){
            List<Integer> removeIdxList = new ArrayList<>();
            // 후에 삭제할 때 인덱스 오류때문에 뒤에서부터 삭제해야함
            // 한 번씩 이동 시킴
            for(int i=list.size() - 1; i>=0; i--){
                boolean b = list.get(i).movePos(intArray);
                // 만약 목적지에 도달한 로봇이 있다면 삭제
                if(!b)
                    removeIdxList.add(i);
            }
            
            for(int idx : removeIdxList){
                list.remove(idx);
            }
            
            // 충돌지점이 있는 지 체크
            for(int[] tmp : intArray){
                for(int val : tmp){
                    if(val > 1){
                        answer++;
                    }
                }
            }
            
        }
        
        
        return answer;
    }
}
