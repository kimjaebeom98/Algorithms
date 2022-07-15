def solution(lottos, win_nums):
    answer = []
    maximum = 0
    minimum = 0
    
    #key = 맞춘 갯수, value = 등수
    count = {'6': 1, '5': 2, '4': 3, '3' : 4, '2': 5, '1': 6, '0' : 6}
    
    cnt = 0
    cnt_0 = 0
    for num in lottos:
        if num == 0:
            cnt_0 += 1
            
        if num in win_nums:
            cnt += 1
    
    minimum = count[str(cnt)]
    for i in range(cnt_0):
        cnt += 1
    maximum = count[str(cnt)]
    
    answer.append(maximum)
    answer.append(minimum)
    
        
    return answer