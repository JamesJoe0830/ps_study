# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYJW0g-qlO8DFASv&categoryId=AYJW0g-qlO8DFASv&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1&&&&&&&&&&
# 14692. 통나무 자르기[D3]
#
# <문제 접근 방법>
# 짝수면 -> Alice 홀수면 -> Bob 출력하면 끝
#
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = int(input())
answer = []


for test_case in range(TC):
    N = int(input().strip())
    if N % 2 == 0 :
        answer.append("Alice")
    else:
        answer.append("Bob")

# 출력 
for i in range(TC):
    print('#{} {}'.format(i+1,answer[i]))

# -----------------------------------------------------------------------------
