from itertools import permutations

def solution(k, dungeons):
  tmp = k
  answer = -1
  for i in permutations(dungeons, len(dungeons)):
    cnt = 0
    for j in i:
      if k >= j[0]:
        cnt += 1
        k -= j[1]
    answer = max(cnt, answer)
    k = tmp
  
  return answer