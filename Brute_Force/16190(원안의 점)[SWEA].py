# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYcllbDqUVgDFASR&categoryId=AYcllbDqUVgDFASR&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1#
# 16910. 원안의 점 [D3]
# 
# <문제 접근>
# 0. 체크하는 부분에서 반지름보다 작거나 같은 정수를 x와 y 에 대입하여 x^2 + y^2 <= R^2 을 만족하면 cnt를 하면 끝이다.
# 
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

answer = []

def check(R):
    cnt = 0
    for x in range(-R,R+1):
        for y in range(-R,R+1):
            if x**2 + y**2 <= R**2:
                cnt +=1
    answer.append(cnt)

T = int(input())
for test_case in range(T):
    N= int(input())
    check(N)

# 출력
for i in range(T):
    print("#{} {}".format(i+1, answer[i]))
# -----------------------------------------------------------------------------