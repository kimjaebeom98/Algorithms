n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []

"""

"""


def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return

    for i in arr:
        if i not in tmp:
            tmp.append(i)
            dfs()
            tmp.pop()


dfs()
