# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWVl3rWKDBYDFAXm&categoryId=AWVl3rWKDBYDFAXm&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=4
# 5431. 민석이의 과제 체크하기 [D3] -> 🧾 정렬
#
# <문제 접근>
# Ok 과제 제출한 애들에 없는 숫자들 arr에 저장하면 끝
#
#
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = int(input())
answer =[]

def Check_list(N,K,Ok):
    global answer
    arr = []
    for i in range(1,N+1):
        if i not in Ok:
            arr.append(str(i))
    answer.append(arr)




for test_case in range(TC):
    N, K =map(int,input().split())
    Ok = list(map(int,input().split()))
    Check_list(N,K,Ok)

for i in range(TC):
    print('#{} {}'.format(i+1,' '.join(answer[i][0:len(answer[i])])))
# -----------------------------------------------------------------------------
