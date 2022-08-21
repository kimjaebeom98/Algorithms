n = int(input())
arr = list(map(int, input().split()))
rm_node = int(input())

def dfs(rm_n):
  arr[rm_n] = 51

  for i in range(len(arr)):
    # 삭제 될 노드를 부모로 가진다면
    if arr[i] == rm_n:
      # chilid 노드의 애들도 없애줘야함
      dfs(i)


dfs(rm_node)
cnt = 0
for i in range(len(arr)):
  if arr[i] != 51 and i not in arr:
    cnt += 1

print(cnt)

