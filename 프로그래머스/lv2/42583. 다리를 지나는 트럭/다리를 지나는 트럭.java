import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int count = 0;
        // 대기 중인 트럭들 Q
        Queue<Integer> waitingQ = new LinkedList<>();
        for(int truck_weight : truck_weights)
            waitingQ.offer(truck_weight);
        // 다리에 건너는 트럭들 Q
        Queue<Integer> bridgeQ = new LinkedList<>();
        for(int i=0; i<bridge_length; i++)
            bridgeQ.offer(0); // 처음은 0으로 초기화(건너는 트럭이 없음)

        int curWeight = weight;
        while(!waitingQ.isEmpty()){
            count++; // 시간은 계속 흐름
            curWeight += bridgeQ.poll(); // 빠져나간 트럭 무게를 더 함
            if(curWeight >= waitingQ.peek()){ // 가용 무게가 허락돼서 들어갈 수 있다면 들어감
                int inputWeight = waitingQ.poll();
                bridgeQ.offer(inputWeight);
                curWeight -= inputWeight; 
            }else{
                bridgeQ.offer(0); // 트럭이 안 들어왔을 때
            }
        }
        while(!bridgeQ.isEmpty()){ // 마지막에 들어오고 큐가 비어서 바로 종료가 됐으니, 끝까지 빠져나오도록 함 
            count++;
            bridgeQ.poll();
        }

        return count;
    }
}
