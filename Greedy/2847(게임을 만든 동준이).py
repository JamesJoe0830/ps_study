# https://www.acmicpc.net/problem/2847 -> 게임을 만든 동준이(실버 4)-> Greedy
# <Greedy인 근거>
# 0. 가장 적게 뺄 수 있는 방법을 고르는 것이기 때문에
# 
# <문제 푸는 방법>
# 0. i+1 이 i 보다 작거나 같으면 i+1의 수 -1 을 i값에 넣어줌
# 1. 원래 배열 - 변경된 배열 값들 더함
# ------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

N = int(input())
points = []
compare = []
answer = 0
for _ in range(N):
    a= int(input())
    points.append(a)
    compare.append(a)

for i in range(N-1):
    if points[(N-1)-i] <= points[(N-1)-(i+1)]:
        points[(N-1)-(i+1)] = (points[(N-1)-i]-1)


for i in range(N-1):
    if compare[i] != points[i]:
        answer += compare[i] - points[i]
print(answer)
# ------------------------------------------------------------------------------
