from sys import stdin

n = int(stdin.readline())

# dp배열의 인덱스 값에 해당하는 숫자의 1을 만드는 최솟 값을 저장
# 사용하기 쉽도록 n+1 사이즈의 배열로 만들어 index 1의 값은 0, index 2의 값은 1 저장

dp = [0 for _ in range(n+2)]

# 처음 두 값은  우리가 아니깐 상향식으로
dp[1] = 0
dp[2] = 1

# 세 가지 경우 다 비교할거임
# 3번,2번 이랑 비교하고, 2번, 1번이랑 비교하고
for i in range(3, n+1):

    dp[i] = dp[i-1] + 1 #3번, x-=1에 해당
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2]+1) #3번, 2번 비교
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3]+1) #2번, 1번 비교

print(dp[n])


