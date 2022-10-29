"""
1 -> 2 -> 3 -> 1이 잇어야함
"""

def solution(ingredient):
    answer = 0
    stk = []
    for i in ingredient:
        stk.append(i)
        if stk[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                stk.pop()
                
    return answer