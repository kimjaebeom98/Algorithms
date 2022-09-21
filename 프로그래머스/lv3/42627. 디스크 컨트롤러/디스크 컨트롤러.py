"""
작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리했을 때의 평균시간 return
heapq를 사용
heapq를 처리시간이 작은 순으로 min_heap 구성
현재 작업을 하고 있는 시간의 시작 부터 종료될때까지 범위를 설정 후 그 범위에 요청시간이 속하면  wait큐에 넣음
"""
import heapq
from collections import deque

def solution(jobs):
    jobs = deque(sorted(jobs, key=lambda x:x[0]))
    st, et, cnt = -1, 0, 0
    wait = []
    total = 0
    n = len(jobs)
    while cnt < n :
        while jobs and st < jobs[0][0] <= et:
            s, p = jobs.popleft()
            heapq.heappush(wait, [p, s])
        
        if len(wait) == 0:
            et += 1
            continue
        else:
            process, start = heapq.heappop(wait)
            st = et
            et += process
            total += et - start
            cnt += 1
    return int(total/n)
                
    

        