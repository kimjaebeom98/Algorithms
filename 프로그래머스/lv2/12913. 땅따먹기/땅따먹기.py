"""
dp인 듯 
dp[i][j] = i행에서 j열을 선택했을 때 최고의 점수
dp[i][j] = 이전행에서 j열을 선택안한 것 들 중 최고 + 현재 land[i][j]
"""

def solution(land):
    # 행의 갯수
    n = len(land)
    dp = [[0 for _ in range(4)] for _ in range(n)]
    for i in range(4):
        dp[0][i] = land[0][i]
    
    # 행
    for i in range(1, n):
        # 열
        for j in range(4):
            _max = 0
            # 이전 열 체크
            for k in range(4):
                if j == k:
                    continue
                _max = max(_max, dp[i-1][k])
            dp[i][j] = _max + land[i][j]
    return(max(dp[n-1]))
    
   