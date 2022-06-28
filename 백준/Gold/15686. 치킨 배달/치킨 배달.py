from itertools import combinations

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append([i, j])
        if board[i][j] == 2:
            chicken.append([i, j])

count = []
result = 100000
for can in combinations(chicken, m):
    temp = 0
    for h in house:
        chi_len = 999
        for j in range(m):
            chi_len = min(chi_len, abs(h[0]-can[j][0])+abs(h[1]-can[j][1]))
        temp+= chi_len
    result = min(result, temp)

print(result)



             

