def solution(distance, rocks, n):
    rocks.sort()
    left = 1
    right = distance
    rocks.append(distance)
    maximum = 0
    while left <= right:
        mid = (left + right) // 2
        # 기준 점
        flag = 0
        # 삭제된 바위 갯수
        del_cnt = 0
        for rock in rocks:
            if rock - flag < mid :
                del_cnt += 1
            else:
                flag = rock
        # 너무 많이 삭제됐으면 거리를 줄임
        if del_cnt > n:
            right = mid - 1
        # 거리를 늘림
        else:
            left = mid + 1
            maximum = max(maximum, mid)    
        
            
    return maximum
                
        
        