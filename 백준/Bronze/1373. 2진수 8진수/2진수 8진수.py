two = input()

remainder = len(two) % 3
result = []
for i in range(len(two)-1, remainder-1 , -3):
    num1 = int(two[i]) 
    num2 = int(two[i-1])*2
    num3 = int(two[i-2])*4
    sum = num1+num2+num3
    result.append(sum)
sum = 0
mul = 1
count = 0
if remainder :
    for i in range(remainder-1, -1, -1):
        sum += int(two[i])*mul
        mul = mul * 2
    result.append(sum)

for i in range(len(result)-1, -1, -1):
    print(result[i], end = '')
    
