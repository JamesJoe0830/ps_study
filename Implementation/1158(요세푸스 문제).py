# https://www.acmicpc.net/problem/1158
# 요세푸스 문제 (1158번) -> 실버4 <구현> ->🔥 오답 필요
# 
# [💡 아이디어 💡]
# <deque을 Que처럼 활용함>
# 1. 앞에 k-1개를 뽑아서 뒤로 갖다 붙이자
# 2. K번째는 빼서 answer에 저장
# <deque의 장점>
# 1.리스트를 활용한 것 보다 빠르다
#
# 
# ----------------------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
Num = deque()
answer = []
for n in range(1, N+1):
    Num.append(n)
print(Num)
while Num:
    # 🔥 핵심 : 앞에 k-1개를 빼서 뒤로 가져다 붙이고 K 번째 뽑아서 answer에 저장 🔥 
    for i in range(K-1): 
        Num.append(Num.popleft()) 
    answer.append(Num.popleft())


print('<{}>'.format(', '.join(map(str, answer))))

# ----------------------------------------------------------------------------------------
# --[문제 풀이 0번]--------------------------------------------------------------------------
# -> 결과는 오답
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# Num = []
# answer = []
# for n in range(1, N+1):
#     Num.append(n)

# now = K-1

# while Num:
#     if len(Num) >= K:
#         if now > len(Num):
#             now -= len(Num)
#         rm = Num.pop(now)
#         answer.append(rm)

#     else:
#         rm = Num.pop(0)
#         answer.append(rm)

#     now += K-1
# print('<{}>'.format(', '.join(map(str, answer))))
# ----------------------------------------------------------------------------------------
