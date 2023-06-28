# https://level.goorm.io/exam/49082/%ED%96%89%EC%84%B1%EC%9D%84-%EA%B4%80%EC%B8%A1%ED%95%98%EB%8A%94-%ED%95%A0%EC%95%84%EB%B2%84%EC%A7%80%EC%9D%98-%EC%9D%B4%EC%95%BC%EA%B8%B0/quiz/1
# 행성을 관측하는 할아버지의 이야기 -> recursion DFS (난이도 4)
#
#
#
#
# --------------------------------------------------------------------------------------------------
N, M = map(int, input().split())
planets = []
for test_case in range(M):
	a, b = map(int, input().split())
	planets.append([a, b])

# [[1,3],[2,3][4,2]]

# recursion DFS_min
def DFS_min(v):
    global planets, visited, minP

    visited.add(v)
    for i in range(M):
        if planets[i][0] == v and planets[i][1] not in visited:
            minP += 1
            # print(minP)
            DFS_min(planets[i][1])

# recursion DFS_max
def DFS_max(v):
    global planets, visited1, maxP

    visited1.add(v)
    for i in range(M):
        if planets[i][1] == v and planets[i][0] not in visited1:
            maxP += 1
            # print('들어온 맥스',planets[i][0])
            DFS_max(planets[i][0])


answer = []
for i in range(1, N+1):
    minP, maxP = 0, 0

    visited, visited1 = set(), set()
    DFS_min(i)
    DFS_max(i)
    answer.append([maxP, minP])
# 출력
for i in range(N):
    print(*answer[i])

# [풀이 방법 .0]----------------------------------------------------------------------------------------
# 시간초과 발생 8번 9번에서
# N, M = map(int, input().split())
# planets = []
# for test_case in range(M):
# 	a, b = map(int, input().split())
# 	planets.append([a, b])

# # [[1,3],[2,3][4,2]]

# # recursion DFS_min
# def DFS_min(v):
#     global planets, visited, minP

#     visited.append(v)
#     for i in range(M):
#         if planets[i][0] == v and planets[i][1] not in visited:
#             minP += 1
#             # print(minP)
#             DFS_min(planets[i][1])

# # recursion DFS_max
# def DFS_max(v):
#     global planets, visited1, maxP

#     visited1.append(v)
#     for i in range(M):
#         if planets[i][1] == v and planets[i][0] not in visited1:
#             maxP += 1
#             # print('들어온 맥스',planets[i][0])
#             DFS_max(planets[i][0])


# answer = []
# for i in range(1, N+1):
#     minP, maxP = 0, 0

#     visited, visited1 = [], []
#     DFS_min(i)
#     DFS_max(i)
#     answer.append([maxP, minP])
# # 출력
# for i in range(N):
#     print(*answer[i])
# --------------------------------------------------------------------------------------------------