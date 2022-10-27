
def solution(n):
    answer = 0
        
    for i in range(1, n//2 + 2):
        tmp = i
        for j in range(i+1, n//2 + 2):
            tmp += j
            if tmp > n:
                break
            elif tmp == n:
                answer += 1
    return answer+1