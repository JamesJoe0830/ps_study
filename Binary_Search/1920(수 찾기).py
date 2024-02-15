# https://www.acmicpc.net/problem/1920
# 1920.수 찾기 [🥈 실버 4]
# 📚 알고리즘 분류: 이진 탐색
# ⏰ 걸린 시간 : 20분
#
#
# [풀이 방법]
# 0. 이진 탐색을 통해서 O(logN)의 시간복잡도를 갖고 문제를 접근한다.
# 1. Flag를 사용해서 못찾았을 경우 print(0)을 해야한다.
# 2. 이진 탐색을 써서 mid 값을 찾아주고 벗어나면 start end를 재설정 해서 탐색한다.
# 3. start와 end는 새로운 값을 찾을때 초기화해준다.
# ------------------------------------------------------------------
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A.sort()
for i in range(M):
    Find = False
    start = 0
    end = N-1
    if B[i] < A[0] or B[i] > A[N-1]:  # 초기에 벗어나는 범위는 0으로 출력
        print(0)
    else:
        while start <= end:
            mid = (start + end) // 2

            if B[i] == A[mid]:
                print(1)
                Find = True
                break
            elif B[i] > A[mid]:
                start = mid + 1
            elif B[i] < A[mid]:
                end = mid - 1
        if Find == False:
            print(0)
# ------------------------------------------------------------------
