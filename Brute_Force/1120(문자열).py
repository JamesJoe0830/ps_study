# https://www.acmicpc.net/problem/1120 -> 문자얄 (실버 4) ->브루트 포스
# <브루트 포스인 이유?>
# 0. 처음부터 끝까지 비교 해야한다. 자리수 별로 다른 것을 cnt해줌
# 
# <문제 접근 방법> -> 겹치지 않는 것이 최소가 되는 것을 출력
# 0. A의 길이가 B의 길이보다 작거나 같다.
# 1. arr: 자리수가 같지 않다면 배열에 저장후 다른 것의 개수 제일 작을때 출력하자
# 2. A와 B의 길이가 같을때 다를때를 나눠서 볼 것
# --------------------------------------------------------------------------

import sys
input =sys.stdin.readline

A, B = map(str,input().split())

# cnt: 다른 개수 세는 것
cnt = 0 
arr = []

 # case1) A와 B의 길이가 같다면
if len(A) == len(B):
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt+=1
    print(cnt)
# case2) A와 B의 길이가 다른 경우 
else:              
    for i in range(0,len(B)-len(A)+1):
        cnt = 0 
        for j in range(len(A)):
            if A[j] != B[i+j]:
                cnt+=1
        arr.append(cnt)
    print(min(arr))

# --------------------------------------------------------------------------
