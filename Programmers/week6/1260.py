import sys
N, M, V = map(int, sys.stdin.readline().split())
# dictionary 에 입력 받아서 저장하기
arr = []
arr1 = 0
needvisit, visited = [],[]
for i in range(M): 
    a, b = map(int, sys.stdin.readline().split())   
    arr.append([a, b])
    arr.append([b, a])
def dfs(n):
    for i in range(len(arr)):
        if arr[i][0] == n and arr[i][1] not in visited:
            needvisit.append(arr[i][1])
            print(needvisit)
            minVal = min(needvisit)
            #print(needvisit , minVal)
    visited.append(n)
    needvisit.clear()
    print(visited)
    dfs(minVal)
def bfs(n):
    for i in range(len(arr)):
        if not visited:
            visited.append(n)
        else:
            if arr[i][0] == n and arr[i][1] not in visited:
                needvisit.append(arr[i][1])
            
            pop_value = needvisit.pop(0)
            visited.append(pop_value)

            
                
dfs(V)


# graph = [0] * 
    #visited = V # 시작과 동시에 방문 번호에 체크
# visited.append(V)

# for j in range(N-1):
#     for i in range(len(arr)):# 5
#             if arr[i][0] ==visited[j]:
#                 if arr[i][1] not in visited:
#                     needvisit.append(arr[i][1])
#             elif arr[i][1] ==visited[j]:
#                 if arr[i][0] not in visited:
#                     needvisit.append(arr[i][0])
#             print(needvisit)
#             visited.append(min(needvisit))
# #print(visited)