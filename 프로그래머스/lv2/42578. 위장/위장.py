def solution(clothes):
    answer = 1
    chk = {}
    for i in clothes:
      if i[1] in chk:
        chk[i[1]] += 1
      else:
        chk[i[1]] = 1
      
    for i in chk.values():
      answer*=(i+1)
        
    

    return answer-1
