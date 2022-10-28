from bisect import bisect_left, bisect_right

n = int(input())
having = list(map(int, input().split()))
m = int(input())
chk = list(map(int, input().split()))

having.sort()

for target in chk:
    left_idx = bisect_left(having, target)
    right_idx = bisect_right(having, target)
    if right_idx - left_idx == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')