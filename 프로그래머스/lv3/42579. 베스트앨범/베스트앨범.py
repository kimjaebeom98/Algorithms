def solution(genres, plays):
    answer = []
    total = {}
    for g, p in zip(genres, plays):
      if g not in total:
        total[g] = p
      else:
        total[g] += p

    play = {}

    total = sorted(total.items(), key = lambda x : x[1], reverse=True) # [(pop, 3100), (classic, 1450)]

    temp = []
    for genre, t in total:
      count = 0
      for j in range(len(genres)):
        if genres[j] == genre:
          temp.append((j, plays[j]))
          count += 1
      if count >= 2:
        temp[len(temp)-count:len(temp)] = sorted(temp[len(temp)-count:len(temp)], key = lambda x : x[1], reverse=True)
        for i in range(count-2):
          temp.pop()




    for i in range(len(temp)):
      answer.append(temp[i][0])
    return answer