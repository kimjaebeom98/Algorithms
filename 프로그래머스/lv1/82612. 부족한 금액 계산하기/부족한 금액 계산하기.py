def solution(price, money, count):
    answer = 0
    res = sum([i*price for i in range(1, count+1)])
    return answer if money >= res else res - money