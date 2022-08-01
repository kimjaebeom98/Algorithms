n, k = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))

cnt = 0
for i in range(n-1, -1, -1):
  if arr[i] <= k:
    cnt += (k//arr[i])
    k %= arr[i]

print(cnt)