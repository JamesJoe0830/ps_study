# https://www.acmicpc.net/problem/2531
# 회전초밥 (2531번) -> 실버1 <브루트포스> ->🔥 오답 필요
#
# [💡 아이디어 💡]
# 0. 회전은 마지막에서 k개 만큼만 접시 앞에꺼를 append시키자
# 1. slice를 해서 c(보너스 초밥) 값 없으면 slice한 것에 넣어주기 
# 
#
# [🔥 오답시 체크 사항 🔥]
# Why? 
# 0. 왜 오히려 deque 보다 list로 했을때 시간초과가 나오지 않는가 ?
# 
# 0. deque에서 slicing 할때
#   0-1. import itertools
#   0-2. list(itertools.islice(리스트,시작,끝))
# ------------------------------------------------------------------------------------------------
import sys

N, d, k, c = map(int, sys.stdin.readline().split())
plates = []


for n in range(N):
    plates.append(int(sys.stdin.readline()))
for i in range(k): # 회전을 해주기 위해서 
    plates.append(plates[i])

# 최대 초밥을 먹을 수 있는 가지수

answer = 0
for n in range(N):
    slice = []
    for i in range(n,n+k):
        slice.append(plates[i])
    if c not in slice:
        slice.append(c)
    answer= max(answer,len(set(slice)))

print(answer)
# ------------------------------------------------------------------------------------------------

# [풀이방법 .0]----------------------------------------------------------------------------------
# 😡시간초과 발생 
# import sys
# from collections import deque
# input = sys.stdin.readline
# import itertools
# N, d, k, c = map(int, input().split())
# plates = deque()


# for n in range(N):
#     plates.append(int(input()))
# for i in range(k):
#     plates.append(plates[i])

# answer = len(set(itertools.islice(plates,0,k)))  # 최대 초밥을 먹을 수 있는 가지수
# if c not in set(itertools.islice(plates,0,k)):
#     answer += 1

# for n in range(1, N):
#     compare = len(set(itertools.islice(plates,n,k+n)))
#     if c not in set(set(itertools.islice(plates,n,k+n))):
#         compare += 1

#     answer = max(answer, compare)

# print(answer)
# ------------------------------------------------------------------------------------------------

# [풀이방법 .1]---------------------------------------------------------------------------------------
# 😡시간초과 발생
# 
# import sys
# from collections import deque
# import itertools
# input = sys.stdin.readline

# N, d, k, c = map(int, input().split())
# plates = deque()


# for n in range(N):
#     plates.append(int(input()))

# answer = len(set(itertools.islice(plates, 0, k)))  # 최대 초밥을 먹을 수 있는 가지수
# if c not in set(itertools.islice(plates, 0, k)):
#     answer += 1

# for n in range(1, N):
#     if n+k-1 > N-1:
#         plates.rotate(-((n+k)-N))
#         n = n-((n+k)-N)
#     sequence = set(itertools.islice(plates, n, n+k))
#     compare = len(set(itertools.islice(plates, n, n+k)))
#     if c not in sequence:
#         compare += 1

#     answer = max(answer, compare)

# print(answer)
# ------------------------------------------------------------------------------------------------
