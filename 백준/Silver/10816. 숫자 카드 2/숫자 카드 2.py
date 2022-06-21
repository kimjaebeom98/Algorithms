from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))

m = int(input())
checks = list(map(int, input().split()))


cards.sort()
j = 0
for i in checks:
    l = bisect_left(cards, i)
    r = bisect_right(cards, i)
    count = r - l
    print(count)
    #checks[j] = count
    #j+=1

