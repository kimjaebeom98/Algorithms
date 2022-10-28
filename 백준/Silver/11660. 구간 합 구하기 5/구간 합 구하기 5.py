import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

s = [[0 for _ in range(n+1)] for _ in range(n+1)]

s[1][1] = arr[0][0]
# 1행
for i in range(2, n+1):
    s[1][i] = s[1][i-1] + arr[0][i-1]
# 1열
for i in range(2, n+1):
    s[i][1] = s[i-1][1] + arr[i-1][0]

for i in range(2, n+1):
    for j in range(2, n+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + arr[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    res = s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]
    print(res)
