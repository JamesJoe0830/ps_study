# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXO72aaqPrcDFAXS&categoryId=AXO72aaqPrcDFAXS&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 10570. 제곱 팰린드롬 수 [D3] -> 📊정렬
# 
# 어떠한 양의 정수 N에 대해서, N과 √N이 모두 팰린드롬이면 이 수를 제곱 팰린드롬 수
# 예를 들어, 121은 제곱 팰린드롬 수인데, 121이 팰린드롬이며, 121의 제곱근인 11 역시 팰린드롬
# ----------------------------------------------------------------------------------------------------
import sys
input = sys.stdin.readline


T = int(input ())

    
for tc in range(1, T+1):
    A, B = map(int,input().split())

    i = A
    cnt =0

    while True:
        if i > B:
            print('#{} {}'.format(tc,cnt))
            break
        sqrt_i = i ** (1/2)

        if sqrt_i % 1 == 0:
            arr = list((str(int(sqrt_i))))
            arr1 = list((str(int(i))))
            reverse_arr = list(reversed(arr))
            reverse_arr1 = list(reversed(arr1))
            if arr == reverse_arr and arr1 == reverse_arr1:
                cnt +=1
        i +=1
  
# ----------------------------------------------------------------------------------------------------




        