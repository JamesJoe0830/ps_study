# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 43162. 네트워크 [🥈 LEVEL 2]
# 📚 알고리즘 분류: BFS&DFS
# ⏰ 걸린 시간 : 3분
# 시간 복잡도 : O(n^2)
# 
# [문제 풀이 & recursion DFS로 문제 푼 근거]
# 0. 네트워크는 결국 연결되어 있는 것을 하나의 그룹으로 본다.
# 0-1. 이때 visited 배열을 통해 재방문 문제를 해결해 나갈 수 있다.
# 1. 그룹을 세는 문제고 하나의 그룹으로 묶고 나오는 것을 따질때는 recursion DFS가 적합하다고 판단했다.
# 2. 그렇지만 BFS로도 문제를 접근해서 풀 수 있다.
# -------------------------------------------------------------------------------------

def solution(n, computers):
    answer = 0
    visited = []
    # recursion DFS
    def DFS(v):
        visited.append(v)
        for i in range(n):
            if computers[v][i] == 1 and i not in visited:
                DFS(i)
    for i in range(n):
        if i not in visited:
            DFS(i)
            answer +=1
    
    return answer
# -------------------------------------------------------------------------------------