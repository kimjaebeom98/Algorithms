def solution(array, commands):
    answer = []
    for li in commands:
      new = array[li[0]-1:li[1]]
      new.sort()
      answer.append(new[li[2]-1])
    
    return answer