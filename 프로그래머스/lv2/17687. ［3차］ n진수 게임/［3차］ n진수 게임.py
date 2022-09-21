"""
자신이 말해야 하는 숫자를 출력하는 프로그램
진법 n, 미리 구할 숫자의 갯수 t, 게임 참여 인원 m, 자신의순서 p
"""

"""

"""

chk = {
    10 : 'A',
    11 : 'B',
    12 : 'C',
    13 : 'D',
    14 : 'E',
    15 : 'F'
}
def n_zin(a, b):
    if a < b:
        if a >= 10:
            a = chk[a]
            return a
        else:
            return str(a)
        
    q = a // b # 15 # 5 # 1
    r = a % b # 0 # 2 # 2
    if r >= 10:
        return str(n_zin(q, b) + chk[r])
    else:
        return str(n_zin(q, b)) + str(r)
    
    
def solution(n, t, m, p):
    tmp = []
    for i in range(0, t*m+1):
        tmp.extend(list(n_zin(i, n)))
    
    step = 1
    res = ''
    for i, k in enumerate(tmp):
        if len(res) == t:
            break
        if i % m == p-1:
            res+=k
    return res
        
         
    
            