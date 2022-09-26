"""
백트래킹
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
base condition = 수들을 담고있는 리스트 길이가 M이면 print()

general condition = 길이가 M이 아니면, start부터 N까지 탐색하면서 
arr에 추가시킴 
"""

n, m = map(int, input().split())
arr = []


def backtracking(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(start, n+1):
        arr.append(i)
        backtracking(i+1)
        arr.pop()


backtracking(1)
