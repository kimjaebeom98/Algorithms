def solution(record):
  chage = {}

  for info in record:
    temp = info.split(' ')
    if temp[0] != 'Leave':
      chage[temp[1]] = temp[2]

  answer = []

  for info in record:
    temp = info.split(' ')
    temp_s = ''
    name = chage[temp[1]]
    if temp[0] == 'Enter':
      temp_s = name + "님이 들어왔습니다."
    elif temp[0] == 'Leave':
      temp_s = name + "님이 나갔습니다."
    else:
      continue

    answer.append(temp_s)
  return answer