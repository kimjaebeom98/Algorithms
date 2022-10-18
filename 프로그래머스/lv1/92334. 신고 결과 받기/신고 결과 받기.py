"""
각 유저는 한 번에 한명의 유저만 신고가능
신고 횟수에 제한은 없음 그러나 같은 유저만 계속해서 신고한다면 신고횟수는 1회로 처리
k번 이상 신고된 유저는 게시판 이용이 정지됨 그 유저를 정지한 사실을 메일로 발송

"""

def solution(id_list, report, k):
    report_cnt = {}
    chk = {}
    # 자기를 신고한사람
    tmp = {}
    res = {}
    for i in id_list:
        report_cnt[i] = 0
        chk[i] = set()
        tmp[i] = []
        res[i] = 0
        
    for re in report:
        # 신고자 신고당한자
        a, b = re.split(' ')
        length = len(chk[a])
        # a가 b를 신고함
        chk[a].add(b)
        # 같은 사람을 신고 했을 때
        if length == len(chk[a]):
            continue
        else:
            report_cnt[b] += 1
            tmp[b].append(a)
    
    
    for key in report_cnt:
        # 자신이 신고를 k번이상 당하면 정지 -> 신고한 사람들에게 메일 보냄
        if report_cnt[key] >= k:
            # 정지먹은 녀석을 신고한 사람들
            for a in tmp[key] :
                res[a] += 1
    
    result = []
    for i in id_list:
        result.append(res[i])
    
    return result
        
            
    