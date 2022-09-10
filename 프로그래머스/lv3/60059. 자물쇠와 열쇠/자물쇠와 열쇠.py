import copy


def rotate(key):
    row = len(key)
    col = len(key[0])

    rotate_key = [[0] * row for _ in range(col)]

    for x in range(row):
        for y in range(col):
            rotate_key[y][row-x-1] = key[x][y]
    return rotate_key


def solution(key, lock):
    # 자물쇠 크기
    n = len(lock)
    # 열쇠 크기
    m = len(key)
    # 3배 큰 자물쇠
    lock_3 = [[0] * (n * 3) for _ in range(n*3)]

    # 3배 큰 자물쇠 중앙에 기존 자물쇠 넣기
    for x in range(n):
        for y in range(n):
            lock_3[n+x][n+y] = lock[x][y]

    # (1, 1) ~ (5, 5)
    for i in range(1, n*2):
        for j in range(1, n*2):
            r_key = copy.deepcopy(key)
            # 회전 시키기
            for _ in range(4):
                for x in range(m):
                    for y in range(m):
                        lock_3[i+x][j+y] += r_key[x][y]

                flag = True
                for x in range(n, n*2):
                    for y in range(n, n*2):
                        if lock_3[x][y] != 1:
                            flag = False
                            break
                    if not flag:
                        break

                if flag:
                    return True
                # 열쇠가 안 맞으니
                # 원상복귀
                for x in range(m):
                    for y in range(m):
                        lock_3[i+x][j+y] -= r_key[x][y]
                # 시계방향으로 회전시켜서 체크
                r_key = rotate(r_key)
    return False
