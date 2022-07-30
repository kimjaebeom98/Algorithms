import heapq

def solution(jobs):
    # start는 처리 시작 시간
    # end는 처리 완료 시간
    # i는 처리한 갯수
    start, end, i = -1, 0, 0
    answer = 0
    hq = []
    while i < len(jobs):
      for job in jobs:
        if start < job[0] <= end :
          # heap을 구성할 때
          # 작업이 빨리 끝나는 순 대로 heap을 구성하기 위해
          # 순서를 바꿈
          heapq.heappush(hq, [job[1], job[0]])

      # 힙이 비어 있으면 job이 요청이 되지 않은 거니깐
      if len(hq) == 0:
        end += 1
      else:
        et, st = heapq.heappop(hq)
        start = end
        end += et
        answer += (end - st)
        i += 1
    return int(answer/len(jobs))