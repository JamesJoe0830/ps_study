# https://www.acmicpc.net/problem/9663
# 9663. N-Queen [🥇 골드 4] -> 🔥 오답 필요
# 📚 알고리즘 분류: 백 트래킹
# ⏰ 걸린 시간 : 시간초과 (백 트래킹 알고리즘으로 처음)
# 
# [백 트래킹 알고리즘 푼 근거 및 회고]
#  0. 가지치기가 필요하다.
#  1. 가지치기 하고 다시 돌아가서 역추적이 필요하다.
#  2. 한 행에는 1개의 퀸만 놓인다. 한 열도 한개만 존재하고
#  3. 대각선상에 하나의 퀸만 존재

# ✔️ [백 트래킹]
# DFS + Promising, Pruning(가지치기)
# * Pruning: 조건에 맞지 않는 가지의 루트는 제거하고 다른 루트로 옮겨 탐색 시간을 절약하는 기법
# * Promising: 확인 단계에서 해당 루트가 조건에 맞는지를 검사하는 기법(유망한지)
# ------------------------------------------------

import sys
input = sys.stdin.readline
N = int(input())
# row는 queen이 각각 row마다 어디에 위치해있는지 [1,3,0,2] -> (0,1) (1,3) (2,0) (3,2) 에 퀸이 있다.
row = [0] * N
answer = 0


# 유망한지 검사
def promising(x) : 
    for i in range(x):
        # 0에서 x 까지 같은 컬럼에 퀸이 있는지 없는지 , 대각선에 퀸이 있는지 없는지
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i) :
            return False
    return True

def n_queen(x):
    global answer
    if x == N:
        answer +=1
        return
    
    else:
        for i in range(N):
            row[x] = i
            # 유망하다면 n_queen을 계속 깊이 탐색
            if promising(x): 
                n_queen(x+1)

n_queen(0)
print(answer)

# ------------------------------------------------