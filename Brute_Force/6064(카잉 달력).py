# https://www.acmicpc.net/problem/6064 -> 카잉 달력(실버 1) -> 정수론(수학) 브루트 포스 -> 오답 필요
# x < M 이면 x' = x + 1이고, 그렇지 않으면 x' = 1이다. 
# 같은 방식으로 만일 y < N이면 y' = y + 1이고, 그렇지 않으면 y' = 1

# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline
ans_list = []

def cal(M, N, x, y):
    answer = x  
    while M * N >= answer: # 결국 최소공배수에 관한 문제 
        if (answer-x) % M == 0 and (answer-y) % N ==0:
            return ans_list.append(answer) 

        answer += M
    return ans_list.append(-1) # 함수가 종료되었다는 return을 통해 예외처리 가능

test = int(input())
for t in range(test):
    M, N, x, y = map(int,input().split())
    cal(M, N, x, y)

# 출력
for _ in range(test):
    print(ans_list[_])

# -----------------------------------------------------------------------------
#  시간 초과 발생 [+1씩 계산하면 시간초과 나옴]
# for t in range(test):
#     M, N, x, y = map(int,input().split())
#     answer = 1
#     if x == y : 
#         ans_list.append(x)
#     else:
#         dx, dy = 1, 1
#         while True:
#             if dx ==x and dy ==y:
#                 ans_list.append(answer)
#                 break
#             elif answer > M * N:
#                 ans_list.append(-1)
#                 break
#             if dx < M :
#                 dx += 1
#             else:
#                 dx = 1
#             if dy < N:
#                 dy += 1
#             else:
#                 dy = 1
#             answer +=1
# for i in range(test):
#     print(ans_list[i])
# -----------------------------------------------------------------------------
