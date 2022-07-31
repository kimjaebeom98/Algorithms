def solution(tickets):
    graph = {}

    for start, end in tickets:
      if start not in graph:
        graph[start] = [end]
      else:
        graph[start].append(end)

    for i in graph:
      graph[i] = sorted(graph[i], reverse=True)


    stk = ['ICN']
    res = []

    while stk:
      cur = stk[-1]
      
      if cur not in graph or not graph[cur] :
        res.append(stk.pop())
      else:
        stk.append(graph[cur].pop())

    res.reverse()
    
    
    return res