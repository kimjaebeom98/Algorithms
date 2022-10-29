"""
연속해서 같은 발음을 못함
네 가지 발음과 발음 조합 밖에 못 함
"""


def solution(babbling):
    initial = ['aya', 'ye', 'woo', 'ma']
    chk = ['ayaaya', 'yeye', 'woowoo', 'mama']
    cnt = 0
    for bab in babbling:
        flag = 0
        for c in chk:
            if c in bab:
                flag = 1
                break
        if flag:
            continue
                
        for i in initial:
            bab = bab.replace(i, ' ')
            
        if not len(bab.strip()):
            cnt += 1
    return cnt