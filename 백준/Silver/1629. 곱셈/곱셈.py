def recur(a, b, c):
    if b == 1:
        return a%c

    if b % 2 == 0:
        return recur(a, b//2, c)**2 % c
    else:
        return (recur(a, b//2, c)**2)*a % c


a, b, c = map(int, input().split())
print(recur(a, b, c))
