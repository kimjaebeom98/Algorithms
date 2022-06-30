n = int(input())
per = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

maximum = -1e9
minimum = 1e9

def dfs(i, result, plus, minus, mul, div):
    global maximum, minimum
    if i == n:
        maximum = max(result, maximum)
        minimum = min(result, minimum)
    
    if plus:
        dfs(i+1, result+per[i], plus-1, minus, mul, div)
    if minus:
        dfs(i+1, result-per[i], plus, minus-1, mul, div)
    if mul:
        dfs(i+1, result*per[i], plus, minus, mul-1, div)
    if div:
        if result < 0:
            dfs(i+1, -(abs(result)//per[i]), plus, minus, mul, div-1)
        else:
            dfs(i+1, result//per[i], plus, minus, mul, div-1)

dfs(1, per[0], plus, minus, mul, div)
print(maximum)
print(minimum)