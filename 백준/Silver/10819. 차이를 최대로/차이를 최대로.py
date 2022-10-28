n = int(input())
arr = list(map(int, input().split()))
_max = 0
visited = [0] * n


def dfs(idx, depth, res):
    global _max
    if depth == n-1:
        _max = max(res, _max)
        return

    for i in range(n):
        if not visited[i]:
            k = abs(arr[idx] - arr[i])
            visited[i] = 1
            dfs(i, depth+1, res+k)
            visited[i] = 0


for i in range(n):
    if not visited[i]:
        visited[i] = 1
        dfs(i, 0, 0)
        visited[i] = 0
print(_max)
