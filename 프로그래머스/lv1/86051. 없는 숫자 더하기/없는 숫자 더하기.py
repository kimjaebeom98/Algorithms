from collections import Counter
def solution(numbers):
    chk = {i : 1 for i in range(10)}
    chk = Counter(chk)
    numbers = Counter(numbers)
    res = chk - numbers
    answer = 0
    for key in res.keys():
        answer += key
    return answer