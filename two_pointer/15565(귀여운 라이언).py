# https://www.acmicpc.net/problem/15565
# 15565. 귀여운 라이언 [🥈 실버 1]
# 📚 알고리즘 분류: 투 포인터
# ⏰ 걸린 시간 : 40분
# 시간복잡도 : O(N)
# 
# [투 포인터 알고리즘 푼 근거 및 회고]
# 0. K개가 있다고 할때 최소의 집합을 결정할때 투포인터를 사용하지 않으면 시간초과 발생
# 
# 
# 문제 풀이
# 0. 1이 있는 인덱스를 추출한다.
# 1. 1의 인덱스 배열의 길이가 K를 넘지 못하면 바로 -1 출력
# 2. 투 포인터로 간격을 좁히며 최소의 집합을 만족하도록 접근
# ------------------------------------------------------------------

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dolls = list(map(int, input().split()))
# 1의 개수가 k일때 길이를 answer라고 놓고 min을 사용해서 업데이트 해준다.
lions = []
for i in range(N):
    if dolls[i] == 1 :
        lions.append(i)
print(lions)

if len(lions) < K:
    print(-1)
else:
    start = 0
    end = 0
    answer = int(10**6)
    while end < len(lions) :
        if  end - start + 1 == K:
            answer = min(lions[end]-lions[start]+1,answer)
            start +=1
        elif end - start + 1 < K:
            end += 1
    print(answer)
# ------------------------------------------------------------------
