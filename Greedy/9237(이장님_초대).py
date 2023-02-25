import sys
N = int(sys.stdin.readline())
day = list(map(int,sys.stdin.readline().split()))
day.sort(reverse=True) # 심는 날이 제일 큰 나무를 앞에서 심어줘야함

invite_day =[] # 초대 날짜 배열로
for i in range(len(day)):
    invite_day.append(day[i]+(1+i))

print(max(invite_day)+1)
