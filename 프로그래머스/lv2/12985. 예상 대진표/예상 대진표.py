"""

"""


def solution(n,a,b):
    cnt = 1
    arr = [i for i in range(1, n+1)]
    while len(arr) != 1:
        tmp = []
        for i in range(0, len(arr)-1, 2):
            if (arr[i] == a and arr[i+1] == b) or (arr[i] == b and arr[i+1] == a):
                return cnt
            elif arr[i] == a or arr[i+1] == a:
                tmp.append(a)
                continue
            elif arr[i] == b or arr[i+1] == b:
                tmp.append(b)
                continue
            else:
                tmp.append(arr[i])
        cnt += 1
        arr = tmp
        
    
    return cnt
        