from collections import deque
n, m = map(int, input().split())
blue = list(map(int, input().split()))

l = max(blue)
r = sum(blue)
while l <= r:
    mid = (l+r)//2

    sum = 0
    count = 0
    for i in blue:
        if sum + i > mid:
            count+=1
            sum = 0
        sum += i
    if sum:
        count+=1

    

    if count <= m:
        r = mid-1
    elif count > m: 
        l = mid+1

print(l)



        
         
    