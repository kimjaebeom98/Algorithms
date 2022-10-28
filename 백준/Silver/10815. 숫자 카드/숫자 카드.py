


n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
target_arr = list(map(int, input().split()))


def binary_search(num):
    l_idx = 0
    r_idx = n-1

    while l_idx <= r_idx:
        mid_idx = (l_idx + r_idx) // 2
        if cards[mid_idx] == num:
            return 1

        elif cards[mid_idx] < num:
            l_idx = mid_idx + 1
        else:
            r_idx = mid_idx - 1
    return 0


for target in target_arr:
    res = binary_search(target)
    print(res, end=' ')
