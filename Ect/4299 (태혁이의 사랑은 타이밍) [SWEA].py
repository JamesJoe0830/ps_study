# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWLv6mx6htoDFAVV&categoryId=AWLv6mx6htoDFAVV&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4
# 4299. 태혁이의 사랑은 타이밍 [D3] -> 📝 수학
#
# <문제 접근 방법>
#  0. 그냥 시간 문제임 시간이 모자르면 앞에서 당겨오는 개념
#
#
# -------------------------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    D, H, M = map(int, input().split())
    answer = 0
    day = D - 11
    hour = H - 11
    minute = M - 11

    if minute < 0:
        hour -= 1
        minute += 60
    if hour < 0:
        day -= 1
        hour += 24
    if day >= 0:
        answer = day*24*60 + hour*60 + minute
        print('#{} {}'.format(t, answer))
    else:
        print('#{} {}'.format(t, -1))
# -------------------------------------------------------------------------------------------------
