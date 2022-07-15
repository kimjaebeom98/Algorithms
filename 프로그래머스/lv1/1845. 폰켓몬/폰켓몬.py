def solution(nums):
    answer = 0
    
    
    s = list(set(nums))

    if len(nums)// 2 >= len(s):
        answer = len(s)
    else:
        answer = len(nums)//2
                    
    return answer