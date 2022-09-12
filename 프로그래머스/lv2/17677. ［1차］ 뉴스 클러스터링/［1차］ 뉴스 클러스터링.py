from collections import Counter

def solution(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    for i, ch in enumerate(str1):
        if ch.isalpha():
            str1[i] = ch.upper()
            
    for i, ch in enumerate(str2):
        if ch.isalpha():
            str2[i] = ch.upper()
    
    new1, new2 = [], []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            new1.append(str1[i] + str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            new2.append(str2[i] + str2[i+1])
    if len(new1) == 0 and len(new2) == 0:
        return 65536

    new1 = Counter(new1)
    new2 = Counter(new2)
    g = new1 & new2
    s = new1 | new2
    u = 0
    d = 0
    for i in g.values():
        u += i
    for i in s.values():
        d += i
    print(u)
    print(d)
    return int((u / d) * 65536)
    
        
            
    