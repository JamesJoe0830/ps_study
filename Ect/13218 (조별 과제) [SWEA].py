# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXzjvCCq-PwDFASs&categoryId=AXzjvCCq-PwDFASs&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# 13218. 조별과제 [D3] -> 📝 수학
# 
# 
# 
# 
# ------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = int(input())

answer = [] 
def Team(N):
    global answer
    team = 0
    team = N // 3
    answer.append(team)



for test_case in range(TC):
    N = int(input())
    Team(N)

# 출력
for i in range(TC):
    print('#{} {}'.format(i+1,answer[i]))
# ------------------------------------------------------------------------------
