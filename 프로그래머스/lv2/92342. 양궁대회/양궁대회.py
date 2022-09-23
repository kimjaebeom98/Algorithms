"""
화살의 개수를 담은 자연수 n
어피치 과녁 점수의 개수를 10점부터 0점까지 순서대로 담은 정수 배열 info
k점을 라이언이 더 많이 맞히면 k점을 라이언이 가져감
k점을 똑같이 맞추면 어피치가 가져감
k점을 0발이면 둘 다 0점
라이언이 가장 큰 점수차이로 우승하기 위해 n발의 화살을 어떤 과녁 점수에 맞혀야 할지 배열로담아 리턴
우승할 수 없으면 -1

info의 i번째 원소는 과녁의 10-i점을 맞힌 화살 개수
n발을 꼭 다써야함
우승할 방법이 여러가지일 경우 가장 낮은 점수를 더 많이 맞힌 경우를 return
가장 낮은 점수를 맞힌 개수가 같을 경우 계속해서 그다음으로 낮은 점수를 더 많이 맞힌 경우를 return
"""
from itertools import combinations_with_replacement
from collections import deque

def solution(n, info):
    comb = []
    for c in combinations_with_replacement(range(11), n):
        comb.append(c)
        
    _max = 0
    res = [-1]
    for c in comb:
        result = [0] * 11
        for score in c:
            result[10-score] += 1
            
        ap = 0
        li = 0
        for l in range(len(result)):
            if not (info[l] == 0 and result[l] == 0):
                if info[l] >= result[l]:
                    ap += 10 - l
                else:
                    li += 10 - l
        ch = li - ap
        if ch > _max:
            _max = ch
            res = result
    
    
    return res
    
            
    
    
                
        
    