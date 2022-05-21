import sys

input = sys.stdin.readline

t = int(input())
arr = [tuple(map(int, input().split())) for _ in range(t)]

arr = sorted(arr, key= lambda x : (x[1], x[0]))

count = 0
t = 0
for start, end in arr:
    if t <= start:
        t = end
        count += 1

print(count)
