n = int(input())

def prime_chk(num):
  for i in range(2, int(num**0.5)+1):
    if num % i == 0:
      return False
  return True

def dfs(i):
  if len(str(i)) == n:
    print(i)
  else:
    for j in range(10):
      chk = i*10+j
      if prime_chk(chk):
        dfs(chk)

dfs(2)
dfs(3)
dfs(5)
dfs(7)