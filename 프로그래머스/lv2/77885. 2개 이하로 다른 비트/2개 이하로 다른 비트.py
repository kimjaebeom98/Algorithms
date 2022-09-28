"""
numbers에 있는 number보다는 크면서,
비트가 서로다른게 2개 이하인 것들 중 제일 작은 녀석을 찾아라!

1.
2진수로 변환bin(num)[2:]해서 xor 연산 ^ 시켜줘서 
count('1') 해주면 갯수가 구해지는데 이러면 시간초과

2.
짝수 일때는 맨 마지막 비트가 0이므로 1로 바꿔주면 바로 반환가능
홀수 일때는 맨 뒤에 있는 0의 인덱스를 찾고 인덱스의 값을
'1'로 바꿔주고 그다음번에있는 인덱스의 값을 '1'로 바꿔줌

"""
def f(num):
    # 짝수일 때
    if num % 2 == 0:
        return num + 1
    # 홀수일 때
    else:
        num = '0' + bin(num)[2:]
        i = num.rfind('0')
        num = list(num)
        num[i] = '1'
        num[i+1] = '0'
        return int(''.join(num), 2)


def solution(numbers):
    res = [f(num) for num in numbers]
    return res




            