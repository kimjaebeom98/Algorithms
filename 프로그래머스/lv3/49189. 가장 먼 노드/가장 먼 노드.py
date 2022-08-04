from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    q = deque([1])
    visited[1] = 0
    while q:
        now = q.popleft()

        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                q.append(i)

    _max = max(visited)
    cnt = 0
    for i in range(len(visited)):
        if _max == visited[i]:
            cnt += 1
    return cnt