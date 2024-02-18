# https://www.acmicpc.net/problem/2805
# 2805.나무 자르기 [🥈 실버 2] 🔥 오답 필요
# 📚 알고리즘 분류: 이진 탐색 
# ⏰ 걸린 시간 : 33분
# 
# [풀이 방법]
# 0. mid값을 잡고 모든 나무를 자르고 양수인 값을 더한다.
# 1. 이를 ans라 할때 이 값이 M과 일치하면 멈춘다.
# 2. start와 end가 start>end가 될때도 빠져나오는데 
# 3. 이때 end 값이 답이다.
# ----------------------------------------------------------------
import sys
input = sys.stdin.readline

# N : 나무의 수 / M : 나무의 길이
N, M = map(int,input().split())
trees_length = list(map(int,input().split()))
trees_length.sort()
start = 1
end = trees_length[-1]


while start <= end :
    mid = (start + end) //2
    

    ans = 0
    for i in range(N):
        if trees_length[i] - mid > 0 :
            ans += trees_length[i] - mid
  
    if ans >= M :
        start = mid + 1
    elif ans < M :
        end =  mid - 1 
print(start)
print(end)
# ❗️주의 사항
# 출력값을 mid를 하려고 시도했다.
# 이진 탐색은 (start+end)//2 연산때문에 무조건 중간값을 고르는게 아니고 더 작은 값을 선택한다.
# 때문에 최종적으로 start와 end가 같은 값이 되면 그 값이 최대 값이 아니라 최대값보다 1 작은값이 된다.
# 따라서 반복문이 끝나고 end를 출력하는 것이 맞다.
# ----------------------------------------------------------------


# 아래처럼 되면 항상 최대값의 ans를 뽑지 못하는 문제가 발생한다.
#     if ans == M:
#         break
#     elif ans > M :
#         start = mid + 1
#     elif ans < M :
#         end =  mid - 1

