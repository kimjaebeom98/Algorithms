from sys import stdin

t = int(stdin.readline())

sum_arr = [0]*t


dp = [0 for _ in range(11)]
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    
for i in range(t):
    n = int(stdin.readline())
    sum_arr[i] = dp[n]

for i in range(t):
    print(sum_arr[i])