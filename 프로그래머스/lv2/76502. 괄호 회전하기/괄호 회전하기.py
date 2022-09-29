from collections import deque

def chk(s):
    stk = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stk.append(i)
        else:
            if not stk:
                return False
            else:
                x = stk.pop()
                if x == '(' and i != ')':
                    return False
                elif x == '[' and i != ']':
                    return False
                elif x == '{' and i != '}':
                    return False
    return len(stk) == 0
                    

    

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        tmp = deque(list(s))
        for _ in range(i):
            k = tmp.popleft()
            tmp.append(k)
            
        if chk(tmp):
            answer += 1
    
    
    return answer