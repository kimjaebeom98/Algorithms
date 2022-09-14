from collections import deque
# 3
# 올바른 괄호 문자열인지 check


def chk3(u):
    if u[0] == ')':
        return False
    u = list(u)
    u = deque(u)
    stk = [u.popleft()]
    while u:
        ch = u.popleft()
        if ch == ')' and stk[-1] == '(':
            stk.pop()
        else:
            stk.append(ch)
    return True
# 2


def chk2(p):
    # 2
    u = ''
    v = ''
    # l = ')', r = '('
    l_cnt = 0
    r_cnt = 0
    if p[0] == ')':
        l_cnt += 1
    else:
        r_cnt += 1
    for idx, data in enumerate(p[1:], 1):
        if data == ')':
            l_cnt += 1
        else:
            r_cnt += 1
        if l_cnt == r_cnt:
            break
    u = p[:idx+1]
    v = p[idx+1:]
    return u, v


def solution(p):
    # 1
    if len(p) == 0:
        return p

    # 2
    u, v = chk2(p)
    # 3
    flag = chk3(u)
    if flag:
        u += solution(v)
        return u

    # 4
    else:
        tmp = '('
        tmp += solution(v)
        tmp += ')'
        u = u[1:len(u)-1]
        u = list(u)
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        tmp += ''.join(u)
        return tmp



