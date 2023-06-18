# https://www.acmicpc.net/problem/2531
#
#
# 💡
#
# 🔥 오답시 체크 사항
# 0. deque에서 slicing 할때
#   0-1. import itertools
#   0-2. list(itertools.islice(리스트,시작,끝))
# ------------------------------------------------------------------------------------------------
import sys
from collections import deque
import itertools
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
plates = deque()


for n in range(N):
    plates.append(int(input()))

answer = len(set(itertools.islice(plates, 0, k)))  # 최대 초밥을 먹을 수 있는 가지수
if c not in set(itertools.islice(plates, 0, k)):
    answer += 1

for n in range(1, N):
    if n+k-1 > N-1:
        plates.rotate(-((n+k)-N))
        n = n-((n+k)-N)
    sequence = set(itertools.islice(plates, n, n+k))
    compare = len(set(itertools.islice(plates, n, n+k)))
    if c not in sequence:
        compare += 1

    answer = max(answer, compare)

print(answer)
