import sys

N = int(sys.stdin.readline())

cnt = 0
arr = []

for i in range(N) :
    arr.append(int(sys.stdin.readline()))
target = max(arr)
for i in range(N-1,-1,-1) :
    if arr[i] != target :
        cnt += 1
    else :
        target -= 1
print(cnt)

# import sys
# N = int(sys.stdin.readline())
# numlist, newlist = [],[]
# count =0
# for i in range(N):
#     number = int(sys.stdin.readline())
#     numlist.append(number)
# numlist1 = sorted(numlist)

# # print(numlist1)
# for i in range(0,N):
#     if numlist[0] > numlist[i] or numlist1 != numlist:
#         if numlist[0]-numlist[1]!=1:
#             newlist.append(min(numlist[1:N]))
#             numlist.remove(min(numlist[1:N]))
#             numlist = newlist +numlist
#             newlist =[]
#             count +=1
#         else:
#             newlist.append(max(numlist[1:N]))
#             numlist.remove(max(numlist[1:N]))
#             numlist = newlist +numlist
#             newlist =[]
#             count +=1
# print(numlist)
# print(count)



