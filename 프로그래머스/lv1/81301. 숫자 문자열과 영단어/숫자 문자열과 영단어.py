def solution(s):
    answer = 0
    di = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx, data in enumerate(di):
        if data in s:
            s = s.replace(data, str(idx))
    
    answer = int(s)        
    return answer