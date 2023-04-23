# https://www.acmicpc.net/problem/10610 -> 30 (실버 4) Greedy
# <풀이 방법>
# 주어진 숫자로 30의 배수 만들 수 있으면 그 수를 만들어서 출력 -> 0만 없으면 결국 3의 배수 문제
# 0이 없으면 -1로 만들기
# 3의 배수가 되려면 모든 수 합이 의 배수가 되면 됨
# --------------------------------------------------------------------------
import sys
input = sys.stdin.readline
N = list(map(int,(input().rstrip())))
sum,answer = 0,''

if 0 not in N :
    print(-1)

else: 
    for n in N :
        sum += n
    if sum % 3 == 0 : # 3으로 나눠진다면 
        N.sort(reverse=True)
        for n in N :
            answer += str(n)
        print(answer)
    else :            # 3으로 안나눠지면 -1 출력
        print(-1)
# --------------------------------------------------------------------------
