from collections import deque

def solution(priorities, location):
    priority = deque()
    for idx, data in enumerate(priorities):
      priority.append([idx, data])

    cnt = 0
    i = 0
    while True:

      flag = 0
      data = priority[0][1]

      for j in priority:
        if j[1] > data:
          flag = 1


      if flag == 1:
        tmp = priority.popleft()
        priority.append(tmp)
      else:
        cnt+=1
        if priority[0][0] == location:
          break
        priority.popleft()

      i += 1
    
    return cnt