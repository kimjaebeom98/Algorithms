n, b = map(int, input().split())

res = ''

if b < 10 :
    while n :
        res = str(n % b)+res
        n//=b
elif b >= 10 :
    while n :
        temp = n % b
        if temp >= 10 :
            res = chr(temp-10+65)+res
            n//=b
        else :
            res = str(n % b)+res
            n//=b

print(res)
