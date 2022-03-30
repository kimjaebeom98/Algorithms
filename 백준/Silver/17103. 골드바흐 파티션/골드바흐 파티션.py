arr = [False, False] + [True]*999999

for i in range(2, int(1000001**0.5)+1):
    if arr[i]:
        for j in range(i+i, 1000001, i):
            arr[j] = False

t = int(input())
nums = [int(input()) for _ in range(t)]

for num in nums :
    cnt = 0
    for i in range(2, num//2+1):
        if arr[i] and arr[num - i]:
            cnt+=1
    print(cnt)
