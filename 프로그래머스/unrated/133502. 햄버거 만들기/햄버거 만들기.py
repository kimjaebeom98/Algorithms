"""
1 -> 2 -> 3 -> 1이 잇어야함
"""

def solution(ingredient):
    answer = 0
    stk = []
    for i in ingredient:
        if len(stk) < 3:
            stk.append(i)
        else:
            stk.append(i)
            if stk[-1:-5:-1] == [1, 3, 2, 1]:
                answer += 1
                for _ in range(4):
                    stk.pop()
                
    return answer