# https://www.acmicpc.net/problem/1065 -> 실버4 (한수) -> 브루트 포스
# <브루트 포스인 근거?>
# 99 이상의 수 부터는 모든 수가 한수인지를 체크해야하기 때문에 브루트 포스임
#  <문제 풀이>
# 0. 선택된 로프의 무게중 가장 작은것을 로프 개수만큼 버틸 수 있음 
# 1. answer의 초기 값을 지정하고 계속 업데이트 하는 방식으로 할 것
# 
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline
X = int(input())
answer = 0

if X <= 99:
    print(X)
elif X > 99:
    answer = 99
    i = 100
    while True:
        if i > X:
            print(answer)
            break
        if i < 1000:
            a=i//100
            b=(i-a*100)//10
            c=(i-a*100-b*10)//1

            if b-a == c-b:
                answer +=1
            i+=1 
        elif i == 1000:
            d=i//1000
            a=(i-d*1000)//100
            b=(i-d*1000-a*100)//10
            c=(i-d*1000-a*100-b*10)//1
            if a-d == b-a and b-a == c-b:
                answer +=1
            i+=1
# -----------------------------------------------------------------------------
