num = int(input())
result = ''
if not num :
    print(0)
    exit()

while num :
    if num % -2 :
        result = '1' + result
        num = num // -2 + 1
    else :
        result = '0' + result
        num = num // -2

print(result)
