def solution(prices):
    answer = []
    for i, data in enumerate(prices):
      flag = 0
      for j in range(i+1, len(prices)):
        if prices[j] < data:
          flag = 1
          answer.append(j - i)
          break
      if flag == 0:
        answer.append(len(prices) - i - 1)
    return answer