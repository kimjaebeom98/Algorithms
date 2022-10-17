from collections import Counter

def solution(X, Y):
    chk_x = Counter(X)
    chk_y = Counter(Y)
    tmp = chk_x & chk_y
    print(tmp)
    # 짝꿍이 존재하지 않으면 '-1' return
    if not len(tmp):
        return '-1'
    # 짝꿍이 0으로만 구성되어 있다면 '0' return
    if len(tmp) == 1 and list(tmp.keys())[0] == '0':
        return '0'
    
    chk = ''
    for key in tmp:
        chk += key*tmp[key]
    sort_chk = list(chk)
    return ''.join(sorted(sort_chk, reverse=True))