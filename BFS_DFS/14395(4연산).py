# https://www.acmicpc.net/problem/14395
# 4연산 (14396 골드 5)=> 🔥 오답 2회
# <BFS 로 푼 근거>
# 0. 최단거리, 최소횟수를 찾기에 적합
# 1. 연산후 숫자가 겹치는 순간 plunnig을 위해 BFS로
# <주의 사항>
# 1. 연산을 해주고 연산자는 어떻게 넣어줄 것인가 ?
# 2. t로 바꾸지 못하는 경우 -1 출력은 어떻게 처리할 것인가 ?
# -------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

s, t = map(int, input().split())
Que = deque()

if s == t:
    print(0)
    sys.exit()


Que.append([s, ''])  # 값, 연산자 삽입
visited = set([s])  # 방문값 기록을 중복없이 해주기 위해서 set함수 사용
found = False  # 찾는 값을 초기에 false로 설정해서 찾았는지 유무 판단

while Que:
    value, opers = Que.popleft()
    if value > int(10**9):  # 값의 범위를 벗어나게 되는 경우
        continue
    if value == t:  # 원하는 값에 도달한다면
        print(opers)
        found = True
        break
    for oper in ('*', '+', '-', '/'):
        if oper == '*':
            next_value = value * value
        elif oper == '+':
            next_value = value + value
        elif oper == '-':
            next_value = value - value
        elif oper == '/':
            next_value = 1
        if next_value not in visited:
            Que.append((next_value, opers+oper))
            visited.add(next_value)
if not found:
    print(-1)
# -------------------------------------------------------
