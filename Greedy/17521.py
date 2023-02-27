import sys
n ,W = map(int,sys.stdin.readline().split()) #n은 요일 / W는 돈
co_list=[] # 각 코인을 넣어줌
for i in range(n):
    coin=int(sys.stdin.readline())
    co_list.append(coin)
amount = 0

# for i in range(n-1):
#     if co_list[i] < co_list[i+1] :
#         if w // co_list[i] > 0:
#             amount = w // co_list[i]
#             w = w - (amount * co_list[i])
#     elif co_list[i-1] - co_list[i]<0 and amount > 0:
#         w = w + amount * co_list[i]
#         amount = 0

# if amount > 0:
#     w = w + amount * co_list[n-1]

# print(w)