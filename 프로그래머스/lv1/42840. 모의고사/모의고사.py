def solution(answers):
    answer = []
    student = [[], [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    cnt = [0]*4
    
    for i in range(1, len(student)):
        j = 0
        k = 0
        while k < len(answers):
            t = answers[k]
            if t == student[i][j]:
                cnt[i] += 1
            j += 1
            k += 1
            if j == len(student[i]):
                j = 0
    _max = max(cnt)
    for idx, data in enumerate(cnt):
        if data == _max:
            answer.append(idx)
    return answer