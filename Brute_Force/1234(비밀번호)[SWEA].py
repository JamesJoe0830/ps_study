# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV14_DEKAJcCFAYD&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# [S/W 문제해결 기본] 10일차 - 비밀번호 [D3]
# 
# <핵심 points>
# 0. 어떻게 뺄 것인가 ? => index out of range를 안내고
# 1. 어떻게 반복문을 멈출 것인가 ?
# 
# <문제 접근>
# 0. 처음부터 하나하나 확인하면서 바로 옆에 있는거와 같으면 둘다 소거 후 다시 반복 
# 1. 핵심은 [문제에서 어떻게 반복문을 멈출것인가 ?]
#   -> 줄였는데 계속해서 num의 길이가 같다면 멈추게 하자! next 와 prev를 활용함
# -----------------------------------------------------------------------------

import sys
input = sys.stdin.readline


answer = []
for _ in range(10):
    N, num = input().split()
    str_num = list(str(num))


    while True: 
        prev=len(str_num)
        if prev == next : # 핵심 : 반복문의 무한루프를 탈출하기 위한 조건
            answer.append("".join(str_num))
            break
        for i in range(len(str_num)-1):
            next=len(str_num)
            if int(str_num[i]) == int(str_num[i+1]):
                del str_num[i]
                del str_num[i]
                break
        
# 출력
for i in range(len(answer)):
    print("#{} {}".format(i+1,answer[i]))
# -----------------------------------------------------------------------------


#1 1234
#2 4123
#3 123123
#4 1234123123
#5 12341
#6 123535
#7 123432141
#8 231231321
#9 12312323
#10 9823






