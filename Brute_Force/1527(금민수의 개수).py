A,B = map(int,input().split())
Q = [4,7]
ans = 0
while len(Q) > 1:
    F = Q[0]
    Q.pop(0)

    if F <= B:
        if A<=F:
            ans +=1
        Q.append(F*10+4)
        Q.append(F*10+7)

print(ans)
# 시간 오류 아래 코드
# import sys
# import time
# start = time.time()
# A, B = map(int,sys.stdin.readline().split())
# count,total  =0, 0
# a=0
# for i in range(A,B+1):
#     a =i 
#     count =0
#     for j in range(len(str(i))):
#         if a//10**(len(str(i))-1-j) -7 ==0 or a//10**(len(str(i))-1-j) -4 ==0:
#             count +=1
#             a = i%10**(len(str(i))-1-j)
#         if count == len(str(i)):
#             total +=1
# print(total)
# end = time.time()
# print(end-start)