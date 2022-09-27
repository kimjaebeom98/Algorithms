n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

tmp = []


def dfs(idx):
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return

    for i in range(idx, len(arr)):
        tmp.append(arr[i])
        dfs(i+1)
        tmp.pop()


dfs(0)
