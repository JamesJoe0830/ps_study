# https://www.acmicpc.net/problem/14501 -> 퇴사(실버3)
# 퇴사(실버3) -> 이거 왜 DP를 이용해야 하는가 .. ? 🔥오답 필요
#
# <문제 접근 방법>
# 0. 크기가 N 인 DP 배열 생성
# 1. 당일 상담이 퇴사 전에 가능할 경우 상담 선택
# 2. 당일 상담이 끝나는 날 중 보상이 가장 큰 날의 보상을 당일 보상에 더한다.
# 3. DP 배열에서 가장 보상이 큰 날을 return
# 
# --------------------------------------------------------------------------
import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    # [상담일, 금액]
    # [[3,10],[5,20],[1,10],[1,20],[2,15],[4,40],[2,200]]
    schedule = [list(map(int,input().split())) for i in range(N)]  

    # N일동안 선택할 수 있는 최대 금액
    dp = [0]* N


    for i in range(N):
        if i+schedule[i][0]<=N:
            dp[i] = schedule[i][1]
            for j in range(i):
                # 이전 상담이 오늘 전에 가능할 경우
                if j + schedule[j][0] <= i :
                    # 이전 상담 금액 + 당일 상담 금액의 최대값 선택
                    dp[i] = max(dp[i], dp[j]+schedule[i][1])
    return max(dp)
print(solution())














# [문제풀이 0]-------------------------------------------------------------------
# import sys
# input = sys.stdin.readline

# N = int(input())
# Task = [0]*(N+1)
# Pay = [0]*(N+1)
# for n in range(1, N+1):
#     T, P = map(int, input().split())
#     Task[n] = T
#     Pay[n] = P
# print(Task)
# d = 1
# answer = 0
# while True:
#     print("answer", d, answer)

#     if d > N:
#         print(answer)
#         break

#     money = Pay[d]
#     if d+Task[d]-1 <= N:
#         for i in range(d, d+Task[d]):
#             if Task[d]+d-1 >= Task[i]+i-1 and Pay[d] < Pay[i]:
#                 d = i
#                 Task[d] = Task[i]
#                 Pay[d] = Pay[i]
#                 money = Pay[i]
#         else:
#             d = d+Task[d] - 1
#     answer += money
#     d += 1
# --------------------------------------------------------------------------