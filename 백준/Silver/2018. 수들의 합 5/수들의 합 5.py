n = int(input())

start = 1
end = 1
s = 1
cnt = 0
# end가 n이라는 것은 끝에 도달
# 끝에 도달 한 경우는 남아 있는 start에서 end 까지 구간의 합이
# n보다 작다는 소리니깐 즉시 종료해줘도 됨
while end != n:
  # 현재 구간에서 한 칸 확장
  # 확장을 하고 확장된 칸을 더해줘야 의미가 있음
  if s < n:
    end+=1
    s+=end
  # 현재 구간에서 한 칸 삭제
  # 먼저 현재 구간에서 한 칸을 삭제해야 앞부분이 변경되는 효과
  elif s > n:
    s-=start
    start+=1
  else:
    cnt += 1
    end+=1
    s+=end

# 마지막 n은 무조건 포함이 되어야 하므로
print(cnt+1)