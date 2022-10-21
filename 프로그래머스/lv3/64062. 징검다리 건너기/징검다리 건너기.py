
def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
        
    return answer
            
#     while True:
#         idx = 0
#         flag = 0
#         while idx < len(stones):
#             if stones[idx] == 0:
#                 flag += 1
#                 if flag >= k:
#                     return person
#                 idx += 1
#                 continue
#             # 돌에 숫자가 있고, flag에 값도 있다면 초기화 시킴
#             # 0, 0, .. 을 지나서 온거니깐
#             elif flag :
#                 flag = 0
            
#             stones[idx] -= 1
#             idx += 1
#         person += 1
#     return person
                
        
            
            