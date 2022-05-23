m, l = map(int, input().split())
locationlist = list(map(int, input().split()))
locationlist.sort()



start = locationlist[0]
end = start + l - 0.5
count = 1
for i in locationlist:
    if i <= end:
        continue
    else:
        count += 1
        end = i + l - 0.5

print(count)


