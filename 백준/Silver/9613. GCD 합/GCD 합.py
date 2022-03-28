def gcd(a, b):
    while b!=0:
        r = a % b
        a = b
        b = r
    return a

t = int(input())
result = []
for i in range(t):
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    sum = 0
    for j in range (n):
        for k in range(j+1, n):
            if arr[j] < arr[k]:
                a_t = arr[k]
                b_t = arr[j]
            else:
                a_t = arr[j]
                b_t = arr[k]
            sum+= gcd(a_t, b_t)
                
    result.append(sum)
    
for i in range(t):
    print(result[i])