n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []


def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return

    for i in range(len(arr)):
        tmp.append(arr[i])
        dfs()
        tmp.pop()


dfs()
