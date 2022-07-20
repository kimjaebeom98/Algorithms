import math

def solution(progresses, speeds):
    answer = []
    new = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]


    idx = 0
    for i in range(len(new)):
      if new[idx] < new[i]:
        answer.append(i - idx)
        idx = i
  
    answer.append(len(new) - idx)
    return answer
    return out