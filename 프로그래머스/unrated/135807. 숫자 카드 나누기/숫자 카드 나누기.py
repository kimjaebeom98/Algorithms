import math

def getgcd(array):
    res = array[0]
    for i in array[1:]:
        res = math.gcd(res, i)
    
    return res


def solution(arrayA, arrayB):
    # 최대 공약수 얻기
    resa = getgcd(arrayA)
    resb = getgcd(arrayB)
    
    answera = 0
    answerb = 0
    if resa != 1:
        flag = 0
        for i in arrayB:
            if i % resa == 0:
                flag = 1
                break
        if not flag:
            answera = resa
    
    if resb != 1:
        flag = 0
        for i in arrayA:
            if i % resb == 0:
                flag = 1
                break
        if not flag:
            answerb = resb
    
    return max(answera, answerb)
    
    
    