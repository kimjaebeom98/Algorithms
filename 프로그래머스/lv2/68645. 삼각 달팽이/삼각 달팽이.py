def solution(n):
    # 삼각형을 이루는 정사각형의 갯수를 세기 위함
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] += dp[i-1] + i
    
    tri = [[0] * i for i in range(1, n+1)]
    # /_ 이런 모양으로 재귀를 돌면 될려나
    # 무슨 숫자로 시작할 지, 어디서 시작할 지
    def chk(start, idx, end):
        nonlocal tri, n
        cnt = start
        # /
        for i in range(idx, n):
            for j in range(len(tri[i])):
                if tri[i][j] == 0:
                    tri[i][j] = cnt
                    cnt += 1
                    break
        # _
        for i in range(len(tri[end-1])):
            if tri[end-1][i] :
                continue
            tri[end-1][i] = cnt
            cnt += 1
        # \
        for i in range(end-2, idx, -1):
            for j in range(len(tri[i])-1, -1, -1):
                if tri[i][j]:
                    continue
                tri[i][j] = cnt
                cnt += 1
                break
        
        return cnt
        
        
        
        
    start = 1
    end = n
    for i in range(n):
        for k in tri[i]:
            if not k:           
                start = chk(start, i, end)
                end -= 1
    res = []
    for i in tri:
        res.extend(i)
    
    return res