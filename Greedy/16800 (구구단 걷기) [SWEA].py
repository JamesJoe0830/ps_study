# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYaf9W8afyMDFAQ9&categoryId=AYaf9W8afyMDFAQ9&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 16800. 구구단 걷기 [D3]
# 
# 
# 
# 
# -----------------------------------------------------------------------------
import sys

input = sys.stdin.readline

TC = int(input())
answer =[]
def Division(n):
    division= []
    global answer

    #약수의 개수 출력은 제곱근으로 해서 시간복잡도를 줄이는게 좋다.
    for i in range(1,int(n**(1/2)) +1): 
        if n % i ==0:
            division.append(i)
            if n // i != i :
                division.append(int(n//i))
    division.sort()

    if len(division) % 2 != 0 :
        x = division[len(division)//2] -1
        answer.append(x*2)
    else:
        x = division[len(division)//2-1] -1 
        y = division[len(division)//2] -1 
        answer.append(x+y)



for test_case in range(TC):
    N = int(input())
    Division(N)

# 출력 
for i in range(TC):
    print("#{} {}".format(i+1, answer[i]))

# -----------------------------------------------------------------------------

