# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYGtoa3qARcDFARC&categoryId=AYGtoa3qARcDFARC&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 14555. 공과 잡초 [D3]  -> 브루트 포스
#
#<브루트 포스인 이유?>
# 0. 모든 자리수를 모두 확인해야 한다.
#
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

T = int(input())
answer = []


def check_Ball(n):
    cnt = 0
    global answer
    for i in range(len(n)-1):
        if n[i] == '(' or n[i] == ')':
            cnt += 1
            if n[i+1] == ')' or n[i+1] == ')':
                cnt -= 1
    if n[len(n)-2] != '(' or n[len(n)-2] != ')':
        if n[len(n)-1] == '(' or n[len(n)-1] == ')':
            cnt += 1
    answer.append(cnt)


for test_case in range(T):
    N = input()
    check_Ball(N)


for i in range(T):
    print('#{} {}'.format(i+1, answer[i]))
# -----------------------------------------------------------------------------

