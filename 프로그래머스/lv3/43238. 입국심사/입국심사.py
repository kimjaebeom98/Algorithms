def solution(n, times):
    answer = 0
    # mid는 mid시간 동안 n명의 사람들이
    #  심사를 모두 마칠 수 있는 시간인지 판단 하는 기준 
    l = min(times)
    r = max(times)*n

    while l <= r:
        mid = (l+r) // 2

        count = 0
        for i in times:
            count += mid // i
            if count >= n:
                break

        if count >= n:
            answer = mid
            r = mid - 1
        elif count < n:
            l = mid + 1
            
    return answer