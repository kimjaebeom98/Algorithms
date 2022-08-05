def solution(s):
  min_len = len(s)
  for i in range(1, len(s)//2+2):
    new_s = ''
    iter = s[:i]
    count = 1
    for j in range(i, len(s)+i, i):
      if s[j:j+i] == iter:
        count+=1
      else:
        if count != 1:
          new_s += str(count)
        
        new_s += iter
        iter = s[j:j+i]
        count = 1
    
    min_len = min(min_len, len(new_s))    
  return min_len
