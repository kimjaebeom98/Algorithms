import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

def binaryserach(target, li):
  l = 0
  r = len(li)-1

  while l <= r:
    mid = (l + r) // 2

    if target == li[mid] :
      return 1
    elif target < li[mid]:
      r = mid - 1
    else:
      l = mid + 1
  
  return 0

a.sort()
for i in b:
  print(binaryserach(i, a))
