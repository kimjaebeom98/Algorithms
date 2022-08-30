top = [0]
for _ in range(4):
  top.append(list(map(str,input())))

k = int(input())

# 반 시계 이동
def re_ro(arr):
  tmp = [0] * 8
  tmp[7] = arr[0]
  for i in range(1, len(arr)):
    tmp[i-1] = arr[i]
  return tmp

def ro(arr):
  tmp = [0] * 8
  tmp[0] = arr[7]
  for i in range(len(arr)-1):
    tmp[i+1] = arr[i]
  return tmp

# -1은 반 시계, 1은 시계
chk = [0] * 5
for _ in range(k):
  # -1은 반 시계, 1은 시계, 0은 회전 x
  chk = [0] * 5
  n, di = map(int, input().split())
  chk[n] = di
  # 반 시계 
    # 자신의 왼쪽 톱니바퀴들
  k = n
  r = di
  # 왼쪽에 있다면
  flag = 1
  while k-1 >= 1:
    # 다른 거라면
    if flag and top[k][6] != top[k-1][2]:
      # 정방향으로 돌림
      r = r * -1
      chk[k-1] = r
    else:
      flag = 0
    k -= 1
  k = n
  r = di
  flag = 1
  while k+1 <= 4:
    if flag and top[k][2] != top[k+1][6]:
      r = r * -1
      chk[k+1] = r
    else:
      flag = 0
    k+=1
 
  for i in range(1, 5):
    if chk[i] == -1:
      top[i] = re_ro(top[i])
    elif chk[i] == 1:
      top[i] = ro(top[i])
    else:
      continue
n_s = 1
total = 0 

for i in range(1, 5):
  if top[i][0] == '1':
    total += n_s
  n_s *= 2

print(total)
