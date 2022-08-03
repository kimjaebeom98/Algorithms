def solution(number, k):
    stk = []
    stk.append(number[0])
    for i in range(1, len(number)):
        while stk and number[i] > stk[-1] and k:
            stk.pop()
            k -= 1
        stk.append(number[i])
    if k > 0:
        stk.pop()
    answer = ''.join(stk)
    return answer
        
        
        