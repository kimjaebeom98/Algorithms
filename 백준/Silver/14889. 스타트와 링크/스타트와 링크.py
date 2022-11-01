from itertools import combinations

n = int(input())
arr = [i for i in range(n)]
arr = set(arr)
visited = [0] * n
board = [list(map(int, input().split())) for _ in range(n)]

min_c = 100 * (n//2) + 1

for comb in combinations(range(n), n//2):

    rest = arr - set(list(comb))
    rest = list(rest)
    comb = list(comb)
    

    sum1 = 0
    sum2 = 0
    for a, b in combinations(comb, 2):
        sum1 += board[a][b]
        sum1 += board[b][a]
    for a, b in combinations(rest, 2):
        sum2 += board[a][b]
        sum2 += board[b][a]
    
    min_c = min(min_c, abs(sum1-sum2))
    
print(min_c)