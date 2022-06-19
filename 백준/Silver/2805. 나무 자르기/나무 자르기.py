n, m = map(int, input().split())
trees = list(map(int, input().split()))

lo = 0
hi = max(trees)
mid = (lo+hi)//2

def get_total_h(h):
    ret = 0
    for j in trees:
        if j > h:
            ret += j-h
    return ret


ans = 0
while lo <= hi:
    if get_total_h(mid) >= m:
       ans = mid
       lo = mid + 1
    else:
        hi = mid - 1
    
    mid = (lo+hi)//2

print(ans)
