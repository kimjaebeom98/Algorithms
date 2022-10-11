import sys

input = sys.stdin.readline
n, h = map(int, input().split())
down = [0] * (h+1)  # 석순
up = [0] * (h+1)

# 석순과 종유석의 크기만 기록하면됨
# 왜냐하면 석순 길이가 5짜리가 있다면
# 5,4,3,2,1 구간은 장애물 크기가 + 1되면 되니깐 그냥
for i in range(n):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(h-1, 0, -1):
    # 위에서 부터 아래로 오기 때문에
    # 높이 i 이상의 모든 석순을 만들 수 있음
    # 예를 들어 높이가 6인 동굴에서 높이 5의 개똥 벌레가
    # 날아갈 때 높이 5이상의 석순에 모두 부딪히기 때문에
    # 배열 5의 값이 높이 5의 개똥벌레가 부딪히는 석순의 개수
    down[i] += down[i+1]

    # 얘는 반대로 생각하면 됨
    up[i] += up[i+1]

_min = n
cnt = 0  # 구간의 수
for i in range(1, h+1):
    if _min > down[i] + up[h-i+1]:
        _min = down[i] + up[h-i+1]
        cnt = 1
    elif _min == down[i] + up[h-i+1]:
        cnt += 1

print(_min, cnt)
