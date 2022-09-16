"""
내가 원하는 문서가 몇 번째로 출력되는지?
heap을 써야 할것 같음
- heap에는 내가 원하는 문서의 위치를 저장하기 위해
인덱스와 값을 넣어놔야함
"""

import heapq
from collections import deque

t = int(input())
for i in range(t):
    # n은 문서의 갯수, m은 궁금한 문서의 위치
    n, m = map(int, input().split())
    # 우선순위
    pri = list(map(int, input().split()))
    # 현재의 최댓값 추적
    heap = []
    # 배열값
    tmp = deque()
    cnt = 1
    for i in range(len(pri)):
        heapq.heappush(heap, (-1)*pri[i])
        tmp.append([i, pri[i]])

    _max = (-1)*heapq.heappop(heap)

    while True:
        idx, val = tmp.popleft()
        # 뒤에 큰 것이 있다면 넘어가고
        if val < _max:
            tmp.append([idx, val])
        # 이제 나올차례라면
        elif val == _max:
            # 내가 찾는 값이라면
            if idx == m:
                break
            new_max = (-1)*heapq.heappop(heap)
            _max = new_max
            cnt += 1
    print(cnt)
