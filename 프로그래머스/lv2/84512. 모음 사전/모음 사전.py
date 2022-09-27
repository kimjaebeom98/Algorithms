"""
사전은 'A', 'E', 'I', 'O', 'U'만 사용하여 만들 수 있는 단어들로 수록되어 있음
즉 'A', 'AA', 'AAA', 'AAAA', 'AAAAA', 'AAAAE', 'AAAAI', 'AAAAO', 'AAAAU', 'AAAE'
...'UUUUU'
"""

from itertools import product


def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    tmp = []
    cnt = 0
    res = 0
    def dfs(start):
        nonlocal word, tmp, cnt, arr, res
        
        if ''.join(tmp) == word:
            res = cnt
            return
        
        if len(tmp) >= len(arr):
            return 
        
        for i in range(len(arr)):
            cnt += 1
            tmp.append(arr[i])
            dfs(i)
            tmp.pop()
    dfs(0)
    return res    
    
            
    