"""
dictionary는 항상 마지막값을 저장함
Enter일 때는 result에 [uid, "님이 들어왔습니다."] 저장
Leave일 때는 result에 [uid, "님이 나갔습니다."] 저장
Change일 때는 chk값 갱신

"""

def solution(record):
    chk = {}
    result = []
    for re in record:
        tmp = re.split(' ')
        if len(tmp) == 2:
            in_out, uid = tmp[0], tmp[1]
        else:
            in_out, uid, name = tmp[0], tmp[1], tmp[2]
        if in_out == 'Enter':
            result.append([uid, "님이 들어왔습니다."])
        elif in_out == 'Leave':
            result.append([uid, "님이 나갔습니다."])
            continue
        chk[uid] = name
    
    for i, data in enumerate(result):
        last = chk[data[0]]
        result[i] = last + data[1]
    
    return result
            