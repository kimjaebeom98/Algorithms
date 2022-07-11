def div(p):
    l_c = 0
    r_c = 0
    for i in range(len(p)):
        if p[i] == '(':
            l_c += 1
        else:
            r_c += 1
        
        if l_c == r_c:
            break
    u = ''
    for k in range(i+1):
        u+=p[k]
    v = ''
    for j in range(k+1, len(p)):
        v+=p[j]
    return u,v

def chk(u):
  if u[0] != '(':
    return False
  else:
    stk = list()
    stk.append(u[0])
    for i in range(1, len(u)):
      if u[i] == '(':
          stk.append(u[i])
      else:
          stk.pop()
    
    if len(stk) == 0 :
      return True
    else:
      return False
    
def solution(p):
    answer = ''
    # 1
    if len(p) == 0:
      return answer
    # 2
    u, v = div(p)
        
    # 3    
    flag = chk(u)
    if flag:
        # 3-1
        return u + solution(v)
    # 4
    else:
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        
        # 4-4
        u = u[1:]
        u = u[:-1]
        for i in range(len(u)):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
                
        return answer

