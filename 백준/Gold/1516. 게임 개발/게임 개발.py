from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
indegree = [0] * (n+1)


for i in range(1, n+1):
    arr = list(map(int, input().split()))
    if len(arr) == 2:
        time[i] = arr[0]
        continue

    time[i] = arr[0]
    for j in arr[1: -1]:
        graph[j].append(i)
        indegree[i] += 1

result = [0] * (n+1)


def wisang():
    q = deque()
    for i in range(1, n+1):
        if not indegree[i]:
            q.append(i)

    while q:
        idx = q.popleft()
        result[idx] += time[idx]

        for i in graph[idx]:
            indegree[i] -= 1
            # 1번 건물을 짓는데 먼저 2번, 3번이 지어져야한다
            # 근데 2번은 짓는데 4초, 3번은 10초
            # 따라서 2번이 먼저 지어지더라도 3번을 지을 때까지 기다려야함
            # 그래서 max값으로 함
            result[i] = max(result[i], result[idx])
            if indegree[i] == 0:
                q.append(i)


wisang()
for i in range(1, n+1):
    print(result[i])
