from itertools import permutations
from collections import deque

n = int(input())
per = list(map(int, input().split()))
op = list(map(int, input().split()))

cal = ['+', '-', '*', '//']

cal_list=[]

for i in range(4):
    if op[i] == 0:
        pass
    else:
        for j in range(op[i]):
            cal_list.append(cal[i])

num_op = list(permutations(cal_list, len(cal_list)))
q = deque(num_op)

max_val = -1e9
min_val = 1e9
while q:
    op_list = q.popleft()
    result = per[0]

    for i in range(1, len(per)):
        if op_list[i-1] == '+':
            result+=per[i]
        elif op_list[i-1] == '-':
            result-=per[i]
        elif op_list[i-1] == '*':
            result*=per[i]
        else:
            if result < 0:
                result = -(abs(result)//per[i])
            else:
                result//=per[i]
    
    max_val = max(max_val, result)
    min_val = min(min_val, result)

print(max_val)
print(min_val)