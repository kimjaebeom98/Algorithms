# 1, 2, 3
# 2, 4, 6
# 3, 6, 9

# 1, 2, 2, 3, 3, 4, 6, 6, 9

n = int(input())
k = int(input())

left = 1
right = k # B[k]가 k보다 큰 수는 나올 수가 없음

while left <= right :
  mid = (left+right)//2

  count = 0
  for i in range(1, n+1):
    count += min(mid//i, n)
  
  if count < k:
    left = mid + 1
  else:
    right = mid - 1

print(left)