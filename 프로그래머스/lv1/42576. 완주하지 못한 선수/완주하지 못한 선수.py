def solution(participant, completion):
    answer = ''

    part = {}
    for i in list(set(participant)):
      part[i] = 0
    
    for i in participant:
      part[i] += 1
    
    for i in completion:
      part[i] -= 1
    
    for key, value in part.items():
      if value:
        answer+=key
    

    return answer