"""
1. k(1~10) 점을 각각 a발, b발 맞췄으면 a>b일때 a가 k점을 가져감,
만약 a == b 이면 어피치가 k점을 가져감 그러나 a == b == 0이면 아무도  안가져감

2. 최종점수가 더 높으면 우승 그러나 최종점수가 같으면 어피치 우승

어피치가 n발을 맞춘 과녁의 점수들(info)이 주어질 때, 라이언이 가장 큰 점수 차이로 우승하기 우히ㅐ n발을 어떤 과녁
점수에 맞춰야 할지 return

info의 i번째 원소는 10-i점을 맞힌 화살 개수(return도 이런식으로 해야함)
라이언이 가장 큰 점수차이로 우승할 수 있는 방법이 여러개이면 가장 낮은 점수를 더많이 맞힌 경우를 return
"""

"""
1. (0~ 10)사이의 점수 중 n개의 화살로 맞힐 수 있는 점수의 중복조합을 뽑아냄
2. 라이언 점수판을 만들어냄
3. 비교하면서 라이언 점수를 구하고, 이 점수가 기존에 max값보다 크면 다 비워냄,
같으면 붙임 
"""       
from itertools import combinations_with_replacement
from collections import deque

def solution(n, info):
    comb = deque()
    for i in combinations_with_replacement(range(11), n):
        comb.append(i)
    
    # [10, 10, 3, 4, 1]
    _max = 0
    res = [-1]
    while comb :
        lion = [0] * 11
        tmp = comb.popleft()
        for c in tmp:
            lion[10-c] += 1
        
        ap = 0
        li = 0
        for l in range(len(lion)):
            if not (info[l] == 0 and lion[l] == 0):
                if info[l] >= lion[l]:
                    ap += 10 - l
                else:
                    li += 10 - l
        ch = li - ap
        if ch > _max :
            _max = ch
            res = lion
    
    return res
            
                
                
        
    