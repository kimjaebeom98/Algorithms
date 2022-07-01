n, m, k = map(int, input().split())

# dp[x][y] <= a가 x개, z가 y개로 만들 수 있는 경우의 수
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

# dp[0][i] 은 z밖에 없는 거니깐 만들 수 있는 경우의 수는 1개
for i in range(m+1):
    dp[0][i] = 1

# dp[i][j] 는 'a', 'z'로 만들 수 있는 경우의 수니깐 
# 맨 앞에 'a'가 오는 것으로 만들 수 있는 경우의 수 dp[i-1][j]
# 맨 앞에 'z'가 오는 것으로 만들 수 있는 경우의 수 dp[i][j-1]
# 의 합 
for i in range(1, n+1):
    # dp[i][0] 은 a밖에 없는 거니깐 만들 수 있는 경우의 수는 1개
    dp[i][0] = 1
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

# n개의 'a'와 m개의 'z'로 만들 수 있는 문자열 중 k번 째
def chk(n, m, k):
    if n == 0:
        print('z'*m)
        return
    elif m == 0:
        print('a'*n)
        return

    # 'a'가 맨 앞에 오는 경우 수dp[i-1][j]와 k를 비교하여
    # k가 더 작으면 맨 앞에 'a'가 위치해야함 
    if dp[n-1][m] >= k :
        print('a', end='')
        chk(n-1, m, k)
    else:
        print('z', end='')
        # 'z'가 맨 앞에 오는 경우 수보다 k가 더 크면
        # 맨 앞에 'z'가 위치해야함
        # 그러나 그 다음 문자를 출력하는데에 있어서
        # z가 앞에 이미 출력되어 있고 뒤에 문자를 판별하는 거니깐
        # 'a'가 맨 앞에 오는 경우의 수를 빼고 k를 전달해야함 
        chk(n, m-1, k-dp[n-1][m])



if dp[n][m] < k:
    print(-1)
else:
    chk(n,m, k)