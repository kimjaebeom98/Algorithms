import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
m = int(input())

parent = [0] * (n+1)

for i in range(1, n+1):
  parent[i] = i

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent,a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  elif b < a:
    parent[a] = b
  else:
    return
  
for i in range(1, n+1):
  l = list(map(int, input().split()))
  for j in range(1, len(l)+1):
    if l[j-1] == 1:
      union_parent(parent, i, j)

route = list(map(int, input().split()))
chk = find_parent(parent, route[0])
flag = 0
for i in route[1:]:
  if find_parent(parent, i) != chk:
    flag = 1
    break

if flag :
  print("NO")
else:
  print("YES")
  
  
  