# factorial에서 해당 number가 몇번 들어가는지 count

def count5(num):
    
    cnt = 0
    while num > 0:
        num = num // 5
        cnt += num

    return cnt

def count2(num):
    
    cnt = 0
    while num > 0:
        num = num // 2
        cnt += num

    return cnt

# 5와 2가 쌍을 이뤄서 10을 만들어 냄 = 0의 갯수
# 따라서 count된 수 중에 더 작은 것을 선택

def min_count(n, m):

    temp5 = count5(n) - count5(m) - count5(n-m)
    temp2 = count2(n) - count2(m) - count2(n-m)

    return min(temp5, temp2)



if __name__ == '__main__':
    n, m = map(int, input().split())
    print(min_count(n, m))
