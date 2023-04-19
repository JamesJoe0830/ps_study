# https://www.acmicpc.net/problem/1026 -> 보물(Greedy) 실버 4
# <접근 방법>
# 0. B의 순위를 매기고 A의 인덱스를 변경하자
# <풀이 방법>
# 그냥 A는 오름차순 B는 내림차순으로 정렬하면 끝남

# ----------------------------------------------------------
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sum = 0 
A.sort()
B.sort(reverse =True)

for i in range(N):
    sum += A[i] * B[i]
# 정답 추출
print(sum)
# ----------------------------------------------------------
