# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 43162. 네트워크 [🥈 LEVEL 2]
# 📚 알고리즘 분류: BFS&DFS
# ⏰ 걸린 시간 : 40분
# 시간 복잡도 : O(n^2)
# 
# [문제 풀이 & BFS로 문제 푼 근거]
# 
# -------------------------------------------------------------------------------------
from collections import deque
def solution(maps):
    # y가 m, x가 n
    n = len(maps)
    m = len(maps[0])

    answer = 0
    Q = deque([(0,0)])
    find = False
    dy=[-1,1,0,0]
    dx=[0,0,-1,1]

    while Q:
        y,x= Q.popleft()
        if y == n-1 and x == m-1:
            find = True
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 :
                # 방문체크를 따로 하지 않아도 되는 이유는 maps[ny][nx]==1 일때만 방문하기 때문이다.
                    maps[ny][nx] = maps[y][x] +1
                    Q.append((ny,nx))
    # print(answer,find)
    if find == True : 
        answer = maps[n-1][m-1]
    else:
        answer = -1
    return answer
# ------------------------------------------------------------------------------------- 