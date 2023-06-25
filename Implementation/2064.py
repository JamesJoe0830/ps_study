# https://www.acmicpc.net/problem/2064
# IP 주소 (2064번) -> 골드4 <구현> 
# [💡 아이디어 💡]
# 
# 
# 
# 
# ---------------------------------------------------------------------------------------------
import sys
input=sys.stdin.readline
N = int(input())
ten = list()
arr = list()


def Check(ten,arr,mask):
    ten_digit, two, two_digit = [], [], []
    mask_ans = []
    address_ans = []
    # 4개의 구간 중 다른 구간 check
    for i in range(0,N):
        for j in range(i,N):
            for k in range(4):
                if ten[i][k] != ten[j][k]:
                    ten_digit.append(k)
    # 4개중 가장 먼저 다른구간이 나오는 값 
    mini = min(ten_digit)


    for i in range(N):
        two_digit.append(str(arr[i][mini]))
    for i in range(N):
        for j in range(i,N):
            for k in range(8):
                if two_digit[i][k] != two_digit[j][k]:
                    two.append(k)
    mini_two = min(two)
    # print(mini, mini_two)
    # 네트워크 주소를 가장 작은 네트워크 구하기 위해서 쪼갬 
    arr_split = []
    for i in range(4):
        arr_split.append(list(map(int,str(arr[0][i]))))


    # 네트워크 마스크 0으로 만들기 -> 3개중 다른 자리수가 제일 작은것 기준
    for i in range(4):
        if i >= mini :
            for j in range(8):
                if j >= mini_two:
                    mask[i][j] = 0
                    arr_split[i][j] = 0
                if mini > i :
                    mask[i][j] = 0
                    arr_split[i][j] = 0
    # print(mask)
    # print(arr_split)
    #네트워크 마스크 10진수로 변환
    for i in range(4):
        mask_str=''
        arr_str=''
        for j in range(8):
            mask_str += str(mask[i][j])
            arr_str += str(arr_split[i][j])
        address_ans.append(str(int('0b'+arr_str,2)))
        mask_ans.append(str(int('0b'+mask_str,2))) # 2진수 10진수로 변환
    print('.'.join(address_ans))
    print('.'.join(mask_ans))
    


for n in range(N):
    a, b, c, d = map(int,input().split('.'))
    mask = [[1]* 8 for _ in range(4)]
    ten.append([a,b,c,d])
    arr.append([(format(a,'08b')),(format(b,'08b')),(format(c,'08b')),(format(d,'08b'))])
Check(ten,arr,mask)







# ---------------------------------------------------------------------------------------------
