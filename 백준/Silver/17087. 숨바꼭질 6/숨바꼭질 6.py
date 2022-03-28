def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

n, s = map(int, input().split())

arr = list(map(int, input().split()))

arr_temp = []
for i in range(n) :
    if arr[i] < s :
        arr_temp.append(s - arr[i])
    else :
        arr_temp.append(arr[i] - s)

arr_comp = []
if n == 1:
    print(arr_temp[0])
elif n == 2:
    arr_comp.append(gcd(max(arr_temp[0], arr_temp[1]), min(arr_temp[0], arr_temp[1])))
    print(arr_comp[0])
else:
    for i in range(1, n-1):
        if arr_temp[i] > arr_temp[i-1]:
            max_num = arr_temp[i]
            min_num = arr_temp[i-1]
        else : 
            max_num = arr_temp[i-1]
            min_num = arr_temp[i]

        arr_comp.append(gcd(max_num, min_num))

    print(min(arr_comp))
        

            

     
