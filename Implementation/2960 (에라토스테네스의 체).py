# https://www.acmicpc.net/problem/2960
# 에라토스테네스의 체 (2960번) -> 실버4 <구현>
# 
# [💡 아이디어 💡]
# 0. arr 에서 소수 찾자마자 check로 보냄
# 1. check 에서는 해당 소수 배수들을 arr에서 지우면서 지워지는 값들 del_count에 저장
# 2. 시간을 줄이기 위해서 # ✅ 여기 # 부분에서 K랑 같아지면 그만돌도록 만듦
# 
# 
# ----------------------------------------------------------------------------------------
import sys

N, K =map (int,sys.stdin.readline().split())
arr = list(range(2,N+1)) 
del_count = []


def check(i,arr,del_count):
    
    m =1 


    while True:
        multiple = i*m 
        if multiple > N:
            break
        if multiple in arr:   
            arr.remove(multiple)
            del_count.append(multiple)
        m += 1
        # ✅ 여기 
        if len(del_count) == K: 
            break


for i in range(2,N+1):
    cnt = 0
    for j in range(2,i+1):
        if i % j == 0 :
            cnt +=1 
    # ✅ 여기 len(del_count) !=K
    if cnt == 1 and i in arr and len(del_count) !=K:
        check(i,arr,del_count)

if len(del_count) == K:
        print(del_count[K-1])

# ----------------------------------------------------------------------------------------






