from collections import Counter

r, c, k = map(int, input().split())
arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

cnt = 0
while cnt <= 100:

    r_len = len(arr)
    c_len = len(arr[0])
    if (r_len > r-1 and c_len > c-1) and arr[r-1][c-1] == k:
        print(cnt)
        exit(0)

    # 행이 열보다 컸을 때
    if r_len >= c_len:
        for i in range(r_len):
            tmp = Counter(arr[i])
            if tmp[0]:
                del tmp[0]
            chk = [(key, tmp[key]) for key in tmp]
            chk = sorted(chk, key=lambda x: (x[1], x[0]))
            li = []
            for x, y in chk:
                li.append(x)
                li.append(y)
            arr[i] = li

        max_len = 0
        for i in range(r_len):
            max_len = max(len(arr[i]), max_len)

        for i in range(r_len):
            for _ in range(max_len - len(arr[i])):
                arr[i].append(0)

    else:
        li = [[] for _ in range(c_len)]
        for i in range(c_len):
            for j in range(r_len):
                li[i].append(arr[j][i])

        r_len = len(li)
        c_len = len(li[0])
        for i in range(r_len):
            tmp = Counter(li[i])
            if tmp[0]:
                del tmp[0]
            chk = [(key, tmp[key]) for key in tmp]
            chk = sorted(chk, key=lambda x: (x[1], x[0]))
            lc = []
            for x, y in chk:
                lc.append(x)
                lc.append(y)
            li[i] = lc

        max_len = 0
        for i in range(r_len):
            max_len = max(len(li[i]), max_len)

        for i in range(r_len):
            for _ in range(max_len - len(li[i])):
                li[i].append(0)

        arr = []
        r_len = len(li[0])
        c_len = len(li)
        arr = [[] for _ in range(r_len)]
        for i in range(r_len):
            for j in range(c_len):
                arr[i].append(li[j][i])

    cnt += 1

print(-1)
