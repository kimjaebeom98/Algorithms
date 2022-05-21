from itertools import combinations

arr = [n*(n+1)//2 for n in range(46)]


def triangle(t):
    for i in range(1, 46):
        for j in range(i, 46):
            for k in range(j, 46):
                if arr[i]+arr[j]+arr[k] == t:
                    return 1
    
    return 0
    
for _ in range(int(input())):
    print(triangle(int(input())))

             