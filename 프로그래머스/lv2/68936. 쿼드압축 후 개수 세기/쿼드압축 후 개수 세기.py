"""
먼저 정사각형이 모두 같은 것으로 이루어진지 확인
이루어져있으면 같은 수로 압축
아니면 4등분해서 또 똑같이 확인하고 압축

"""

            
            

def solution(arr):
    answer = [0, 0]
    l = len(arr)
    
    def divide(a, b, r):
        tmp = arr[a][b]
        
        for i in range(a, a+r):
            for j in range(b, b+r):
                if tmp != arr[i][j]:
                    r =  r // 2
                    divide(a, b, r)
                    divide(a, b+r, r)
                    divide(a+r, b, r)
                    divide(a+r, b+r, r)
                    return
                
        answer[tmp] += 1
        return 
                    
    divide(0, 0, l)
    return answer
    