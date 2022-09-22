def solution(n, computers):
    chk = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j]:
                chk[i].append(j)
    visited = [0] * n
    def dfs(idx):
        nonlocal visited, chk
        visited[idx] = 1
        
        for i in chk[idx]:
            if not visited[i]:
                dfs(i)
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    
    return count
        
                
    