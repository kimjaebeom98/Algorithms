import sys
input = sys.stdin.readline

n = int(input())
train = [0] + list(map(int, input().split()))
limit = int(input())

s = [0 for _ in range(n+1)]
for i in range(1, n+1):
    s[i] = s[i-1] + train[i]

# dp[n][m] 소형 기관차 n대를 운영할 때 m번째 객차를 선택했을 때
# dp[1][n] : n번째 객차까지 1개의 소형 기관차를 사용했을 때
# 운송할 수 있는 최대 손님 수
# dp[2][n] : n번째 객차까지 2개의 소형 기관차를 사용했을 때
# 운송할 수 있는 최대 손님
dp = [[0 for _ in range(n+1)] for _ in range(4)]

for i in range(1, 4):
    for j in range(i*limit, n+1):
        if i == 1:
            # 소형기관차 1대를 운영했을 때,
            # 이전에 구한 최댓 값과, 현재 객차번째에서 이전 limit 객차까지 끌었을때의값 중 큰 값
            dp[i][j] = max(dp[i][j-1], s[j] - s[j-limit])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-limit]+(s[j]-s[j-limit]))

print(dp[3][n])
