n = int(input())
ws = [int(input()) for _ in range(n)]

if n == 1:
    print(ws[0])
    exit()

ws.sort(reverse=True)
_max = ws[0]
for i in range(1, n):
    _max = max(_max, ws[i]*(i+1))

print(_max)
