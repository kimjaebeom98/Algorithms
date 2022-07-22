import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
for idx ,i in enumerate(arr):
  s = 0
  e = n-1
  flag = 0
  while s < e:
    if idx == s:
      s+=1
      continue
    if idx == e:
      e-=1
      continue

    if arr[s] + arr[e] > i:
      e-=1
    elif arr[s] + arr[e] < i:
      s+=1
    else:
      flag = 1
      break

  if flag :
    cnt += 1
print(cnt)