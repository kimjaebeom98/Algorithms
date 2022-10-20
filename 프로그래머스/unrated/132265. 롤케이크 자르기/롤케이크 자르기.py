from collections import Counter

def solution(topping):
    right = Counter(topping)
    left = {}
    cnt = 0
    for i in range(len(topping)):
        tmp = topping[i]
        if tmp not in left:
            left[tmp] = 1
        else:
            left[tmp] += 1
        
        right[tmp] -= 1
        if not right[tmp]:
            del right[tmp]
        
        if len(left) == len(right):
            cnt += 1
        
    return cnt