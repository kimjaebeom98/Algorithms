from collections import deque

def solution(n, wires):
    answer = n+1
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for start, pre_visit in wires:
        visited = [0] * (n+1)
        visited[pre_visit] = 1
        
        # bfs
        q = deque([start])
        visited[start] = 1
        cnt = 1
        while q:
            chk = q.popleft()
            # chk와 연결되어 있는 노드들 탐색
            for i in graph[chk]:
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
                    cnt += 1
        # 한 쪽 전력망 네트워크에 포함되는 송전탑 갯수를 찾으면
        # 자동으로 n-(한쪽 송전탑 갯수)가 다른 쪽 네트워크의 송전탑 갯수
        res = abs(cnt - (n-cnt))
        if res < answer:
            answer = res
        
    return answer