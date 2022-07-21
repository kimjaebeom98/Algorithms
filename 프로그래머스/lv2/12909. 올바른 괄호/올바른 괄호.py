def solution(s):

    stk = []
    for data in s:
        if len(stk) == 0 and data ==')':
            return False
        
        if data == '(':
            stk.append(data)
        else:
            stk.pop()
            
    if not len(stk):
        return True
    
    return False
    