"""
k 앞으로 점프하면 k 만큼의 건전지를 사용함
순간이동을 하면 현재 위치의 x2의 위치로 이동함

n거리에 도달할려고할 때 건전지를 최소로 쓸 수 있는 최소값?
1 2 4 8 16 32 ...
 
"""

def solution(n):
    if n == 1:
        return 1
    
    if n % 2 == 0:
        return solution(n//2)
    else:
        return solution(n-1) + 1


# def solution(n):
#     dp = [0] * (n+1)
#     # 무조건 점프 
#     dp[1] = 1
#     for i in range(2, n+1):
#         # 이전꺼에서 그대로 점프해서 온 거
#         dp[i] = min(dp[i-1] + 1, i)
#         if i % 2 == 0:
#             dp[i] = min(dp[i], dp[i//2])
        
#     return dp[n]