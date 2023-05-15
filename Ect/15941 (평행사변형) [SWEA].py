# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYVgOZEKOpcDFAQK&categoryId=AYVgOZEKOpcDFAQK&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 15941. 평행사변형 [D3]
# 
# 
# 
# 
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = int(input())
answer = []
for test_case in range(TC):
    N = int(input())
    answer.append(N*N)

# 출력
for i in range(TC):
    print("#{} {}".format(i+1, answer[i]))