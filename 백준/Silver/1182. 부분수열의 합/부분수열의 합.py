"""
백트래킹으로 문제를 접근
해당 숫자를 포함해도 되고 안해도 되고가 관점

"""

n, s = map(int, input().split())

arr = list(map(int, input().split()))
visited = [False]*(n)

cnt = 0


def backtracking(idx, _sum):
    global cnt
    if n == idx:
        if _sum == s:
            cnt += 1
        return

    backtracking(idx+1, _sum)
    backtracking(idx+1, _sum+arr[idx])


backtracking(0, 0)
if s == 0:
    cnt -= 1

print(cnt)