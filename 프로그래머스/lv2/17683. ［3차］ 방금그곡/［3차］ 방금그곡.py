"""
시작, 끝, 음악제목, 음
음의 길이보다 재생된 시간의 길이가 더 길면 반복 재생
음의 길이보다 재생된 시간의 길이가 더 짧으면 재생된 시간만큼만 재생
1. 재생된 시간만큼 출력되는 음을 구하고 배열을 저장해야겟슴 그 음들과 배열의 인덱스를 저장

"""
def replace_s(s):
    s = s.replace('C#', 'c')
    s = s.replace('D#', 'd')
    s = s.replace('F#', 'f')
    s = s.replace('G#', 'g')
    s = s.replace('A#', 'a')
    return s


def solution(m, musicinfos):
    answer = []
    for idx, music in enumerate(musicinfos):
        start, end, title, s = music.split(',')
        s = replace_s(s)
        m = replace_s(m)
        # 분을 구함
        h1, m1= start.split(':')
        h2, m2 = end.split(':')
        total = (int(h2) - int(h1))*60 + (int(m2) - int(m1))
        # 재생된 시간만큼 출력되는 음을 구하자
        n = len(s)

        if n < total:
            q = total // n
            r = total % n
            res = q*s + s[:r]
        elif n > total:
            res = s[:total]
        else:
            res = s
        
        
        if res.find(m) != -1:
            answer.append([idx, total, title])
    if len(answer):
        answer = sorted(answer, key = lambda x : (-x[1], x[0]))
        return answer[0][2]
    else:
        return '(None)'
            