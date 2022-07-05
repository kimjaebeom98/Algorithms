s = input()


def dfs(idx, c, maxN):
  global flag, ans
  if flag :
    return
  if idx == len(s):
    if c == maxN:
      flag = True
      ans = ' '.join(map(str, temp)) 
    return

  i = int(s[idx])
  if not visit[i]:
    temp[c] = i
    visit[i] = 1
    dfs(idx+1, c+1, maxN)
    visit[i] = 0
    
  
  if idx+1<len(s) :
    i = int(s[idx]+s[idx+1])
    if i <= maxN and not visit[i]:
      visit[i] = 1
      temp[c] = i
      dfs(idx+2, c+1, maxN)
      visit[i] = 0
  
if len(s) < 10:
  new_s = list(int(i) for i in s)
  for k in new_s:
    print(k, end=' ')
else:
  flag = 0
  i = 0

  while flag == 0:
    cur = s[i] + s[i+1]
    r_len = 9 + (2*(int(cur) - 10))
    if r_len == (len(s)-2):
      flag = 1
    i+=1
  
  
  cur = int(cur)
  visit = [0 for _ in range(cur+1)]
  temp = [0 for _ in range(cur)]
  flag = False
  dfs(0, 0, cur)
  print(ans)
     
  