"""
1. s에 0을 모두 제거(cnt += 1)
2. s에서 0을 제거한 새로운 문자열 tmp의 길이 x를 2진법으로 표현한 새로운 문자열 s

1, 2를 s가 '1'이 될때 까지 반복

이진변환의 횟수, 그 과정에서 제거된 0의 갯수
"""
def s_to_2(x):
    x = int(x)
    tmp = []

    while x > 0 :
        r = x % 2 # 0 0 
        x = x // 2 # 2 1
        tmp.append(str(r))
    tmp.reverse()
    
    return ''.join(tmp)


def solution(s):
    new_s = s
    # 제거된 0의갯수
    cnt = 0
    # 이진변환 횟수
    count = 0
    while new_s != '1':
        tmp = ''
        for i in new_s:
            if i == '0':
                cnt += 1
                continue
            tmp += i

        # 0을 제거한 문자열의 길이를 2진법으로 변환
        new_s = s_to_2(len(tmp))
        count += 1
    
    return(count, cnt)
    
    
    
        
    
    
    