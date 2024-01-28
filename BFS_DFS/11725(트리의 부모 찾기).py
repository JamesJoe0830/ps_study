# https://www.acmicpc.net/problem/11725
# 11725. 트리의 부모 찾기 [🥈 실버 2] -> ✨ BFS로 풀어볼 것
# 📚 알고리즘 분류: BFS&DFS
# ⏰ 걸린 시간 : 60분
# 시간복잡도 : O(N)
# 
# [오래 걸린 이유]
# 0. 처음 접근은 부모노드들을 어떻게 최신화 할까 ? 였다.
# 1. 접근을 각각 노드마다 접근해서 마지막 1을 방문하게 한다면 해당 노드의 부모노드 값을 처음 방문했던 노드로 설정하려했다.
# 2. 너무 어려운 접근이였고 복잡했다.
# 3. 결국 1의 루트 노드부터 접근을 모든 부모를 1로 설정하고 계속 부모노드를 최신화 시켜주면 되는 문제였다.
# [문제 접근 방법]
# 0. 1번이 루트 노드이기 때문에 1번에서 출발해서
# 1. 자식들을 방문하면서 그때마다 부모의 node를 최신화한다.
# 
# [recursion DFS 알고리즘 & linked list  푼 근거 및 회고]  
# 0. linked list는 시간복잡도를 N^2에서 V+E 이렇게 줄여준다.
# 1. 1이 루트노드라서 1부터 DFS로 탐색한다.
# 2. 방문하지 않은 노드의 경우에 부모 노드의 값을 answer에 넣어준다.
# 3. 깊이 탐색을 재귀로 하면서 각각을 최신화 할 수 있다.
# ---------------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
# setrecursionlimit(10**5) 이렇게 하면 메모리 초과가 나오지 않는다.
# setrecursionlimit(10**5) 이렇게 하면 메모리 초과가 발생한다.
# 미리 메모리를 할당하는 것이기 때문에 스택 영역을 적게 잡아야한다.
N=int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (N+1)
answer = [0] * (N+1)
def DFS(node,visited):
    visited[node] = 1
    for next_node in tree[node]: 
        if not visited[next_node]: # 방문하지 않은 노드의 값을 본다. 
            answer[next_node]=node # 방문하지 않은 노드의 값을 부모 노드로 설정한다. node가 부모
            DFS(next_node,visited)

DFS(1, visited)
for i in range(2,N+1):
    print(answer[i])
# ---------------------------------------------------------------------------------------------