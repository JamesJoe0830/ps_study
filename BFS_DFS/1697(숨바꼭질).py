# BFS를 이용 / QUEUE
import sys
N, K = map(int,input().split())
max_value =100001
visited = [0]*(max_value)
Queue =[]

Queue.append(N)
while Queue : # Queue에 데이터가 있다면 계속 돌아라 !
    node = Queue.pop(0)
    if node == K : # while문을 멈춰줌 
        print(visited[node])
        break
    for next in (node-1,node+1,2*node): # for 문의 처음 써보는 구문 세가지를 next로 넣어줌
            if 0<= next < max_value and not visited[next] :
                visited[next] = visited[node] +1
                Queue.append(next)
#print(visited[next])

# for i in range(3):
#     if node -1 not in visited and node-1 not in needvisit:
#         needvisit.append(node -1)
#     elif node +1 not in visited and node+1 not in needvisit:
#         needvisit.append(node +1)
#     elif 2*node not in visited and 2*node not in needvisit:
#         needvisit.append(2*node)

# for i in range(100):
#     if i==0 :
#         if count ==1:
#             print(0)
#     else:
#         if 3**i <= count < 3**(i+1):
#               print(i+1)