# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7IzvG6EksDFAXB&categoryId=AV7IzvG6EksDFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
# 2817. 부분 수열의 합 [D3] -> 경우의 수 
# 
# 
# <문제 접근 방법>
# 0. 2중 for 문을 돌면서 K와 일치하면 count 해줌 
# 
# ------------------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = int(input())
answer = []
def Subsequence(N,K,arr):
    global answer
    cnt = 0
    for i in range(N):
        for j in range(N):
           if arr[i]+arr[j] ==K and i !=j:
            cnt+=1
            break
    answer.append(cnt)



for test_case in range(TC):
    N, K = map(int, input().split())
    arr = list(map(int,input().split()))
    Subsequence(N,K,arr)

# 출력
for i in range(TC):
    print('#{} {}'.format(i+1,answer[i]))