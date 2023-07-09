# https://www.acmicpc.net/problem/15686
# 15686. 치킨 배달 [골드5]  -> Implementation 🔥 오답 필요
#  
# <💡 Combination>
# 0.집과 치킨집의 좌료를 각각 리스트에 저장
# 1. M개의 치킨집 선택하는 것이 관건 combination을 통해 가능한 조합중에 min이 되는 것을 추출한다.
# 
# 
# -----------------------------------------------------------------------------
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
# 0은 빈 칸, 1은 집, 2는 치킨집이다.

graph = [list(map(int,input().split())) for _ in range(N)]
house= []
chicken =[]
answer = (N+1)**5

# 각각의 집좌표 치킨 좌표 저장
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            house.append((x,y))
        elif graph[x][y] == 2:
            chicken.append((x,y))

# M개의 치킨집 선택하는 것이 관건 combination을 통해 가능한 조합중에 min이 되는 것을 추출한다.
for chi in combinations(chicken,M): # M개의 치킨집 선택
    total_distance = 0 # 계속 비교할 총 거리 
    for (xh,yh) in house:
        distance = (N+1)*(N+1)
        for (xc,yc) in chi:
            curr_distance = abs(xh-xc)+abs(yh-yc)
            distance = min(distance, curr_distance)
        total_distance +=distance
    answer = min(answer, total_distance)

print(answer)

# -----------------------------------------------------------------------------
# fre_chicken= []
# distances= []
# for (xh,yh) in house:
#     distance = N*N
#     min_xc,min_yc = 0, 0
#     for (xc,yc) in chicken:
#         curr_distance = abs(xh-xc)+abs(yh-yc)
#         if distance > curr_distance:
#             min_xc=xc
#             min_yc=yc
#             distance = min(distance, curr_distance)

#         print(min_xc,min_yc)
#     fre_chicken.append((min_xc,min_yc))
#     distances.append(distance)
# counter = Counter(fre_chicken).most_common()
# print('fre',fre_chicken)
# print(counter)
# print(distances)
# answer = 0


