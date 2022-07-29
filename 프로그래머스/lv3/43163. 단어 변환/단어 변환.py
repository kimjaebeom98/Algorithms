def solution(begin, target, words):
  if target not in words:
    return 0
  
  visited = [0]*len(words)
  flag = 0
  c = 0
  def dfs(word, target, words, visited, count):
    nonlocal flag, c
    
    if target == word:
      flag = 1
      c = count
      return
    if flag :
      return

    for i in range(len(words)):
      if not visited[i]:
        cnt = 0
        for j in range(len(word)):
          if word[j] != words[i][j]:
            cnt+=1
        if cnt == 1:
          visited[i] = 1
          dfs(words[i], target, words, visited, count+1)
          visited[i] = 0 
  
  dfs(begin, target, words, visited, 0)
  if flag :
    return c
  else:
    return 0