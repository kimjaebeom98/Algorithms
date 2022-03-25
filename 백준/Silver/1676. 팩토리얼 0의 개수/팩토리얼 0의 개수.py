def fact(n):
    if n > 1:
        return n * fact(n-1)
    else:
        return 1
## math 패키지에 factorial 함수가 따로 있긴 함

num = int(input())
factorial = fact(num)
string = str(factorial)
string = list(string)
string.reverse()
count = 0

for i in string:
    if i != '0':
        break
    count+=1

print(count)