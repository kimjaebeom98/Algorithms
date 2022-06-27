from collections import deque
import sys
input = sys.stdin.readline 
n, p = map(int, input().split())

melody = [deque() for _ in range(n+1)]
cnt = 0




for i in range(n):
    k, plat = map(int, input().split())
    # k줄에 손가락이 아무것도 없으면
    if len(melody[k]) == 0:
        melody[k].append(plat)
        cnt+=1
        continue
    
    temp_plat = melody[k][-1] 
    
    # 가장 높은 음을 누르고 있는 손가락 보다 더 큰 음이 주어지면
    if plat > temp_plat :
        cnt+=1 
        melody[k].append(plat) # 그냥 손가락으로 누르기  
    
    # 가장 높은 음을 누르고 있는 손가락 보다 작은 음이 주어지면
    elif plat < temp_plat :
        
        # 주어진 음이랑 같거나 작아질 때까지 손가락 떼기
        while melody[k] and melody[k][-1] > plat:
            melody[k].pop()
            cnt+=1

        if len(melody[k]) != 0 and melody[k][-1] == plat:
            continue
        melody[k].append(plat)
        cnt+=1
    # 가장 높은 음을 누르고 있는 손가락 보다 같은 음이 주어지면
    else: 
        continue

print(cnt)
             



