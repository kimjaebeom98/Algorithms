
def solution(skill, skill_trees): 
    answer = 0
    stk = list(skill)
    for i in skill_trees:
        flag = 0
        for j in i:
            if j in stk:
                if j != stk[0]:
                    flag = 1
                    break
                else:
                    stk.pop(0)
        if not flag:
            answer+=1
        stk = list(skill)
    return answer
    
    
    