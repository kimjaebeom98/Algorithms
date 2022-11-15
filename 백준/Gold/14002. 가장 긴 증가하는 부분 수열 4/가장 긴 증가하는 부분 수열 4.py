n = int(input())
arr = list(map(int, input().split()))

# 가장 긴 증가하는 부분순열의 크기
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)


cnt = max(dp)
res = []
for i in range(n-1, -1, -1):
    if dp[i] == cnt:
        cnt -= 1
        res.append(arr[i])

res.reverse()
print(max(dp))
for i in res:
    print(i, end=' ')