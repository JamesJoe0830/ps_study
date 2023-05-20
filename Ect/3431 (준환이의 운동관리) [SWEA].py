# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWE_ZXcqAAMDFAV2&categoryId=AWE_ZXcqAAMDFAV2&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5
# 3431. 준환이의 운동관리 [D3] 
# 
# 
# 
# 
# -------------------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

T = int(input())

for t in range(1,T+1):
    L, U, X = map(int, input().split())
    if X < L:
        answer = L-X
    elif L <= X <= U :
        answer = 0
    elif X > U:
        answer = -1
    print('#{} {}'.format(t, answer))

# -------------------------------------------------------------------------------------------------
