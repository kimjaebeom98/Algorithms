"""
먼저 문자열 처리부터 진행해줘야 함
alpha는 모두 lower로 만들고 [HEAD, NUMBER, TAIL]을 저장함

"""

from collections import deque

def solution(files):
    arr = []
    for file in files:
        tmp = deque(list(file))
        Head = ''
        # HEAD 부분
        while tmp and True:
            ch = tmp.popleft()
            if ch.isdigit():
                tmp.appendleft(ch)
                break
            Head += ch.lower()
        Num = ''
        while tmp and True:
            ch = tmp.popleft()
            if not ch.isdigit():
                tmp.appendleft(ch)
                break
            Num += ch
        Tail = ''
        while tmp:
            ch = tmp.popleft()
            if ch.isalpha():
                ch = ch.lower()
            Tail += ch
        
        arr.append([Head, Num, Tail, file])
    
    arr = sorted(arr, key=lambda x : (x[0], int(x[1])))
    res = [file[3] for file in arr]
    return res
    
            
                