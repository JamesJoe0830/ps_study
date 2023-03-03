import sys
N = int(sys.stdin.readline())
arr = [0]*10001
for i in range(N):
    num = int(sys.stdin.readline())
    arr[num] +=1
for i in range(10001):
    if arr[i]: # 배열이 참일때 즉, 0이 아닐때 
        for j in range(arr[i]):
            print(i)
##################
# arr에 모두 저장하게 되면 메모리가 초과됨 
# 해당 숫자를 만날때마다 값을 올려주는 식으로 코드를 구성하면 메모리 초과 안나옴