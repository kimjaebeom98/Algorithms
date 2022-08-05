def solution(n, words):
    answer = []
    turn = 1
    pre = words[0]
    l = [pre]
    for idx, s in enumerate(words[1:], 1):
        if idx % n == 0:
            turn += 1
        
        if pre[-1] != s[0]:
            return [idx%n + 1, turn]
        elif s in l:
            return [idx%n + 1, turn]
        l.append(s)
        pre = s
        
    return [0, 0]