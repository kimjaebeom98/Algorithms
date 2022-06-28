i = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    
    mod = (v // p)*l
    mod += min((v%p), l)

    print('Case %d: %d' %(i, mod))
    i+=1

