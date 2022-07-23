s, p = map(int, input().split())
sentence = input()
a, c, g, t = map(int, input().split())


start = 0
end = 1
chk = {'A':0, 'C':0, 'G':0, 'T':0}

for i in range(p):
  chk[sentence[i]] += 1

start = 0
end = p-1
cnt = 0
while end != s:
  if chk['A'] >= a and chk['C'] >= c and chk['G'] >= g and chk['T'] >= t :
    cnt += 1
  
  chk[sentence[start]] -= 1
  start += 1
  end += 1
  if end == s:
    break
  chk[sentence[end]] += 1

print(cnt)