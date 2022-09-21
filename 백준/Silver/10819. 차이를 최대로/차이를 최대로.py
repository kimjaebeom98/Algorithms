n = int(input())
a = list(map(int, input().split()))
visited = [0 for _ in range(n)]
per = []

m = 0
def dfs(li):
  global m
  if len(li) == n:
    res = 0
    for i in range(n-1):
      minus_res = abs(li[i] - li[i+1])
      res += minus_res
    m = max(m, res)
    return
  
  for i in range(n):
    if visited[i] == 0:
      visited[i] = 1
      li.append(a[i])
      dfs(li)
      visited[i] = 0
      li.pop()  


dfs(per)
print(m)