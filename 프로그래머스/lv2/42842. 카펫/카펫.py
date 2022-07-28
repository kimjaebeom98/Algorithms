def solution(brown, yellow):
    # a는 행, b는 열
    # 2b + 2*(a-2) == brown
    # (a-2)*(b-2) == yellow
    # 두 조건 만족해야 함
    _sum = brown + yellow
    
    for a in range(2, _sum+1):
        if _sum % a == 0:
            b = _sum // a
            if (a-2)*(b-2) == yellow:
                # 답이 [a, b]아니면 [b,a]가 나오는데
                  # 바로 리턴이면 a가 b보다 작을 때 값이 리턴 될 것임
                  # 따라서 a가 세로, b가 가로 
                return [b, a]
            
    return answer