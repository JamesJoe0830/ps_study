# https://www.acmicpc.net/problem/1010
# 1010. 다리 놓기 [🥈 실버5]
# 📚 알고리즘 분류: DP 🔥오답 필요
# ⏰ 걸린 시간 : 32분
# 시간 복잡도 : O(n)
# [문제 풀이]
# 0. 겹치지 않게 값을 구하려고 한다.
# 1. 조합을 통해서 mCn을 하면 결국 겹치는 선이 저절로 제거된다.
# 2. 이유는 이미 겹치지 않을때 선택한 걸로 결정이 되기 때문이다.
# ---------------------------------------------

import sys
T = int(input())

def factorial(n):
    num = 1
    while n >= 1 :
        num *= n
        n -= 1
    return num

for test_case in range(T):
    N, M = map(int,input().split())
    answer = factorial(M) /(factorial(M-N)*factorial(N))
    print(int(answer))

# ---------------------------------------------