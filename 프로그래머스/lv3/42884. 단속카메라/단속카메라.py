
def solution(routes):
    routes.sort(key = lambda x : x[1])
    chk = -30001
    cnt = 0
    for route in routes:
        if chk < route[0]:
            cnt += 1
            chk = route[1]
    return cnt
        
        
        
        