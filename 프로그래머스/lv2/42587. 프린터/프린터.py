"""
내가 요청한 문서가 몇 번째로 인쇄되는지
1. 내가 요청한 문서가 무엇인지 알기 위해서는 초반에 [우선순위, index]로 새로 배열을 만듬
2. 아직 빠져나가지 못한 것 중 젤 큰 우선순위 추적
3. 한 개를 뽑고, 만약 이것보다 큰 우선순위가 있으면 맨뒤로, 아니면
지금까지 젤 큰 우선순위라는 소리니깐 내가 찾는것인지 비교
"""
from collections import deque

def solution(priorities, location):
    cnt = 1
    _max = deque(sorted(priorities, reverse=True))
    new = deque([[data, idx] for idx, data in enumerate(priorities)])
    
    while True:
        pri, idx = new.popleft()
        if _max[0] > pri:
            new.append([pri, idx])
        else:
            if idx == location:
                return cnt
            else:
                _max.popleft()
                cnt += 1
    
            
                
                