def solution(enroll, referral, seller, amount):
    chk = {}
    p = {}
    # p는 돈 받는 거 기록
    for i in enroll:
        if i not in p:
            p[i] = 0
    # 자신을 추천할 사람이 없으면 그냥 지나가고
    # 추천한 사람이 있으면 chk에 자기가 돈을 줄 사람을
    # 기록
    for idx, refer in enumerate(referral):
        if refer == '-':
            continue
        if enroll[idx] not in chk:
            chk[enroll[idx]] = refer

    def recur(name, money):
        nonlocal chk, p
        if money < 1:
            return
        tmp = money // 10
        p[name] += (money - tmp)
        if name not in chk:
            return

        recur(chk[name], tmp)

    # 판매 집계
    for idx, sell in enumerate(seller):
        # 자신이 돈을 준 사람이 없으면 그대로 가짐

        if sell not in chk:
            p[sell] += int((amount[idx] * 100) * 0.9)
        else:
            recur(sell, amount[idx]*100)

    res = []
    for key in p:
        res.append(p[key])

    return res