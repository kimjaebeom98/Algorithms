import math

def solution(n, stations, w):
    answer = 0
    # 기지국 좌/우 구간들을 구함
    distance = []
    
    for i in range(1, len(stations)):
        distance.append((stations[i] - w - 1) - (stations[i-1] + w) )
    
    if stations[0] - w > 1:
        distance.append(stations[0]-w-1)
    
    if stations[-1] + w < n:
        distance.append(n - (stations[-1] + w))
    
    cnt = 0
    able = 2*w + 1
    for i in distance:
        cnt += math.ceil(i / able) 
    return cnt

    