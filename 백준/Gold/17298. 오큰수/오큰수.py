import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

stk = []
result = [-1 for _ in range(n)]
for i in range(len(a)):
    while stk and a[stk[-1]] < a[i]:
        idx = stk.pop()
        result[idx] = a[i]
    stk.append(i)

for k in result:
    print(k, end = ' ')