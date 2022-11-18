from collections import deque

n, k = map(int, input().split())
# a[i][0]는 내구도, a[i][1]은 로봇이 있는지 없는지
belt = deque(map(int, input().split()))
robots = deque([0]*2*n)


step = 0
while True:
    step += 1

    # 1
    belt.rotate(1)
    robots.rotate(1)
    # 내리는 자리는 즉시 내림
    robots[n-1] = 0

    # 2
    for i in range(n-2, -1, -1):
        if robots[i] and not robots[i+1] and belt[i+1] >= 1:
            belt[i+1] -= 1
            robots[i], robots[i+1] = 0, 1
    robots[n-1] = 0

    # 3
    if not robots[0] and belt[0]:
        robots[0] = 1
        belt[0] -= 1

    # 4
    if belt.count(0) >= k:
        break

print(step)
