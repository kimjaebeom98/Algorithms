from collections import deque
def solution(s):
    
    if s[0] == ')':
        return False
    s = deque(list(s))
    stk = []
    while s:
        ch = s.popleft()
        if ch == '(':
            stk.append(ch)
        else:
            if stk and stk[-1] == '(':
                stk.pop()
            # else:
            #     stk.append(ch)
    if stk:
        return False
    else:
        return True