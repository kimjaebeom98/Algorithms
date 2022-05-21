import sys
from collections import deque


for _ in range(int(input())):
    dq_left = deque()
    dq_right = deque()

    for ch in input():
        if ch == '<' :
            if len(dq_left):
                dq_right.appendleft(dq_left.pop())
        elif ch == '>':
            if len(dq_right):
                dq_left.append(dq_right.popleft())
        elif ch == '-':
            if len(dq_left):
                dq_left.pop()
        else:
            dq_left.append(ch)
    
    print(''.join(dq_left) + ''.join(dq_right))