# 완전 탐색은 불가능
def str_to_int(str_time):
    h = int(str_time[:2]) * 3600
    m = int(str_time[3:5]) * 60
    s = int(str_time[6:]) 
    return h + m + s


def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"
    
    # 0초 부터 시작인데 +1을 해주는 이유는 
    # 시청이 끝난 시간에 -1을 해줄려고
    dp = [0] * (str_to_int(play_time) + 1)
    # log들을 모두 탐색하며, log하나당 범위 내를 모두 마킹하는 것은 n^2임 
    # 그래서 log 하나 씩 시청 시작시간에 + 1을 하고, 
    # 완료 시간에 시청자 수가 빠져나갔으니깐 -1을 함
    
    for log in logs:
        log = log.split('-')
        start = str_to_int(log[0])
        end = str_to_int(log[1])
        dp[start] += 1
        dp[end] -= 1
    
    # dp[i]는 i 시점의 시청 자 수 이다.
    for i in range(1, str_to_int(play_time)):
        dp[i] = dp[i] + dp[i-1]
    

    max_adv = 0
    max_idx = 0
    tmp = sum(dp[:str_to_int(adv_time)])
    max_adv = tmp
    for i in range(str_to_int(adv_time), str_to_int(play_time)):
        tmp = tmp + dp[i] - dp[i-str_to_int(adv_time)]
        if tmp > max_adv:
            max_adv = tmp
            max_idx = i - str_to_int(adv_time) + 1                                        
    
    answer = '%02d:%02d:%02d' % (max_idx / 3600, max_idx / 60 % 60, max_idx % 60)
    return answer
        
        
            
            
        