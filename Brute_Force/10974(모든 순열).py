# https://www.acmicpc.net/problem/10974
# 10974. 모든 순열 [🥈 실버 3] -> permutations(순열) 이용
# 📚 알고리즘 분류: 브루트 포스
# ⏰ 걸린 시간 : 5분
# 시간복잡도 : O(N!)
# 
# 
# [풀이 방법]
# 1. 파이썬 내장 함수인 permutations를 통해서 쉽게 풀 수 있다.
# 2. list(permutations(arr, N)) 이렇게 하면 쉽게 풀 수 있다.
# ------------------------------------------------

import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
arr = []

for i in range(1,N+1):
    arr.append(i)

answer=list(permutations(arr,N))


for row in answer:
    print(*row)
# ------------------------------------------------