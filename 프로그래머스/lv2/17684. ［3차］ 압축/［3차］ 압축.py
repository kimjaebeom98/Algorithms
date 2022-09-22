"""
A-Z 까지의 딕셔너리 초기화 
사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다

"""
from collections import deque

def solution(msg):
    answer = []
    tmp = {}
    # 65 - 90 = A - Z
    # for i in range(65, 91):
    #     tmp[i-64] = chr(i)
    
    for i in range(65, 91):
        tmp[chr(i)] = i-64
    idx = 26
    stk = ''
    msg = deque(msg)
    while msg:
        m = msg.popleft()
        stk += m
        if stk not in tmp:
            idx += 1
            answer.append(tmp[stk[:-1]])
            tmp[stk] = idx
            stk = stk[-1]
        else:
            continue
    if stk:
        answer.append(tmp[stk])
    
    return answer
            
            
            
            
    