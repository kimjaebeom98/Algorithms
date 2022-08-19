n = int(input())
p = list(map(int, input().split()))
dp = [0]*len(p)

for i in range(1, len(p)):
  for j in range(i, 0, -1):
    if p[j] < p[j-1]:
      p[j-1], p[j] = p[j], p[j-1]
    else:
      break 

dp[0] = p[0]
for i in range(1, len(p)):
  dp[i] = dp[i-1] + p[i]

print(sum(dp))
    