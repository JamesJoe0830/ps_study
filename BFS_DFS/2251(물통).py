# https://www.acmicpc.net/problem/2251 (골드 5) 물통 => 오답 필요 (물을 옮기는 Idea)
# 이게 왜 BFS DFS 이지 ?
# <BFS 로 푼 근거>
# 0. 중복된 물통들 가지치기
# 1. 깊이 탐색시 끝까지 다 돌고 plunning 하기 BFS 알고리즘이 더 적합
# 2. 물을 옮길 수 있는 경우의 수는 총 6가지이다.(x->y, x-z, y->x, y->z, z->x, z->y)

from collections import deque
import sys
input = sys.stdin.readline


A, B, C = map(int, input().split())
Bottle = []
C_Bottle = []
Que = deque()
# [(0,0,10),(8,0,2),(0,9,1),(0,8,2),(1,0,9),(8,1,1),(0,1,9),(2,0,8),(0,2,8),(2,0,8),(1,9,0)]

def BFS():
    global C
    Que.append((0, 0, C))

    while Que:
        x, y, z = Que.popleft()
        C = x+y+z
        state = (x, y, z)

        # 물 옮기는 6가지 -> water 를 min 을 통해 접근하는 핵심! (오답)
        # x->y
        if x == 0 and z not in C_Bottle:
            C_Bottle.append(z)
        water = min(x, B-y)
        if (x-water, y+water, z) not in Bottle:
            Que.append((x-water, y+water, z))
            Bottle.append((x-water, y+water, z))
        # x->z
        water = min(x, C-z)
        if (x-water, y, z+water) not in Bottle:
            Que.append((x-water, y, z+water))
            Bottle.append((x-water, y, z+water))
        # y->x
        water = min(y, A-x)
        if (x+water, y-water, z) not in Bottle:
            Que.append((x+water, y-water, z))
            Bottle.append((x+water, y-water, z))
            
        # y->z
        water = min(y, C-z)
        if (x, y-water, z+water) not in Bottle:
            Que.append((x, y-water, z+water))
            Bottle.append((x, y-water, z+water))
        # z->x
        water = min(z, A-x)
        if (x+water, y, z-water) not in Bottle:
            Que.append((x+water, y, z-water))
            Bottle.append((x+water, y, z-water))
        # z->y
        water = min(z, B-y)
        if (x, y+water, z-water) not in Bottle:
            Que.append((x, y+water, z-water))
            Bottle.append((x, y+water, z-water))

BFS()
C_Bottle.sort()
print(*C_Bottle)
