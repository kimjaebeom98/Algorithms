# 현재 정점, 양의 수, 늑대의 수, 현재 노드에서 이동 가능한 노드들

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for p, c in edges:
        graph[p].append(c)
    max_sheep = 0
    
    def dfs(cur, sheep, wolf, nodes):
        nonlocal graph, info, max_sheep
        if not info[cur]:
            sheep+=1
            max_sheep = max(max_sheep, sheep)
        else:
            wolf+=1
        
        if sheep <= wolf:
            return
        
        nodes.extend(graph[cur])
        for node in nodes:
            dfs(node, sheep, wolf, [i for i in nodes if i != node ])
    dfs(0, 0, 0, [])
    return(max_sheep)
            
            
    
    
    
        