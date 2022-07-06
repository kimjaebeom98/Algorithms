from collections import deque

cnt = 0
for _ in range(int(input())):
  word = input()
  word_l = len(word)
  stk = deque()
  flag = 0
  stk.append(word[0])
  i = 1
  while word_l > i :

    if len(stk) and word[i] == stk[-1]:
      stk.pop()
      i+=1
    else:
      stk.append(word[i])
      i+=1
  if len(stk) == 0:
    cnt+=1
  
print(cnt)