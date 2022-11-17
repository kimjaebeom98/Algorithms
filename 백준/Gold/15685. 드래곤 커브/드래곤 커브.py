n = int(input())

# 동북서남
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def chk(x, y, d, g):
    di = []
    di.append(d)
    for _ in range(g):
        for j in range(len(di)-1, -1, -1):
            di.append((di[j] + 1) % 4)
    return di


tmp = set()
for i in range(n):
    x, y, d, g = map(int, input().split())
    res_di = chk(x, y, d, g)
    nx = x
    ny = y
    tmp.add((nx, ny))
    for di in res_di:
        nx += dx[di]
        ny += dy[di]
        tmp.add((nx, ny))

cnt = 0
for i in tmp:
    x, y = i
    if (x-1, y) in tmp and (x, y-1) in tmp and (x-1, y-1) in tmp:
        cnt += 1

print(cnt)
