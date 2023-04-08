# https://www.acmicpc.net/problem/5585 -> (브론즈 2) 거스름돈
# 1000 - 380 = 620 (500엔 1개 / 100엔 1개 / 10엔 2개)
import sys
input = sys.stdin.readline

N = int(input()) # 지불할 돈
changeList = [500,100,50,10,5,1]
pay = 1000 #카운터에 낸 금액
changes = pay - N
cnt = 0

while changes != 0:

    for i in range(len(changeList)):
        if changes - changeList[i] >= 0:
            changes = changes - changeList[i]
            cnt +=1
            break
print(cnt)

