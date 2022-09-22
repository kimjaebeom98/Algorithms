"""
dfs로 풀것
dfs에 인자로 idx와 _sum을 보냄
만약 idx가 len(numbers)와 같으면 그냥 return
만약 _sum이 target값과 같으면 res+=1
"""
def solution(numbers, target):
    def dfs(idx, _sum):
        nonlocal numbers, target
        if idx+1 == len(numbers):
            if _sum == target:
                return 1
            return 0
        
        return dfs(idx+1, _sum + numbers[idx+1]) + dfs(idx+1, _sum - numbers[idx+1])
    
    return dfs(0, numbers[0]) + dfs(0, numbers[0]*(-1))
    