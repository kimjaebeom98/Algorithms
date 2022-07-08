
n, k = map(int, input().split())
use = list(map(int, input().split()))

multi = []
cnt = 0
for i, val in enumerate(use):
  if val in multi:
    continue

  elif len(multi) < n:
    multi.append(val)
  
  else:
    cnt += 1
    max_idx = (-1,0)
    flag = 0
    for j, data in enumerate(multi):
      if data in use[i+1:] :
        idx = use[i+1:].index(data)
        if idx > max_idx[0]:
          max_idx = (idx, j)
      else:
        flag = 1
        multi[j] = val
        break
    
    if not flag:
      multi[max_idx[1]] = val

print(cnt)




      

      

    

  


