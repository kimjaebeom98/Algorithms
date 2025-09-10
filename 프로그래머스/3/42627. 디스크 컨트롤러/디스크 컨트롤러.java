import java.util.*;

class Solution {
    
    public int solution(int[][] jobs) {
        // 작업 종료 시간
        int end = 0;
        // 수행한 작업의 갯수
        int count = 0;
        // 종료 시간의 합
        int answer = 0;
        // 우선순위 큐에 넣은 작업의 idx
        int jobIdx = 0;
        // 소요시간이 빠르면 우선순위
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        // 요청시간이 빠른 순으로 정렬
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
        
        while(count < jobs.length){
            while(jobIdx < jobs.length && jobs[jobIdx][0] <= end){
                pq.offer(jobs[jobIdx++]);
            }
            
            // 현재 시간이 작업 요청 시간보다 빠르기 때문에 작업 요청 시간으로 현재 시간을 돌려줌
            if(pq.isEmpty()){
                end = jobs[jobIdx][0];
            }else{
                int[] tmp = pq.poll();
                // 요청해서 시간 만큼 기다리고(-)
                // 현재시간에서 소요시간 만큼 더하고(+)
                answer += tmp[1] + end - tmp[0];
                end += tmp[1];
                count++;
            }
        }
        
        
        return answer / jobs.length;
    }
}