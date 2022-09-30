import sys
input = sys.stdin.readline
n, l = map(int, input().rstrip().split())
board = list(list(map(int, input().rstrip().split())) for _ in range(n))
answer = 0
# 행
for i in range(n):
  # flag = 1은 지나갈 수 없는 길이라는 뜻
  flag = 0
  # 행은 고정
  chk = [0] * n
  for j in range(1, n):
    # 높이가 2이상 차이나면 경사로를 설치해도 안댐
    if abs(board[i][j] - board[i][j-1]) >= 2:
      flag = 1
      break
    else:
      # 이전 높이가 더 크면 오른쪽에 경사로를 설치해야함
      if board[i][j] < board[i][j-1]:
        for k in range(l):
          # 범위를 벗어나거나 이미 경사로 설치가 되어있거나 경사로를 설치할 공간이 안 나올때
          if k+j >= n or chk[k+j] or board[i][k+j] != board[i][j]:
            flag = 1
            break
          
          if board[i][j+k] == board[i][j]:
            chk[j+k] = 1
      # 현재 높이가 더 크면 왼쪽에 경사로 설치
      elif board[i][j] > board[i][j-1]:
        for k in range(l):
          if j-k-1 < 0 or chk[j-k-1] or board[i][j-k-1] != board[i][j-1]:
            flag = 1
            break

          if board[i][j-k-1] == board[i][j-1]:
            chk[j-k-1] = 1

  if not flag:
    answer += 1
 


# 열
for i in range(n):
  # flag = 1은 지나갈 수 없는 길이라는 뜻
  flag = 0
  # 행은 고정
  chk = [0] * n
  for j in range(1, n):
    # 높이가 2이상 차이나면 경사로를 설치해도 안댐
    if abs(board[j][i] - board[j-1][i]) >= 2:
      flag = 1
      break
    else:
      # 이전 높이가 더 크면 오른쪽에 경사로를 설치해야함
      if board[j][i] < board[j-1][i]:
        for k in range(l):
          # 범위를 벗어나거나 이미 경사로 설치가 되어있거나 경사로를 설치할 공간이 안 나올때
          if k+j >= n or chk[k+j] or board[k+j][i] != board[j][i]:
            flag = 1
            break
          
          if board[j+k][i] == board[j][i]:
            chk[j+k] = 1
      # 현재 높이가 더 크면 왼쪽에 경사로 설치
      elif board[j][i] > board[j-1][i]:
        for k in range(l):
          if j-k-1 < 0 or chk[j-k-1] or board[j-k-1][i] != board[j-1][i]:
            flag = 1
            break

          if board[j-k-1][i] == board[j-1][i]:
            chk[j-k-1] = 1

  if not flag:
    answer += 1

print(answer)


  