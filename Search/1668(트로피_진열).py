import sys
N=int(sys.stdin.readline())

trophy = list()
for i in range(N):
    trophy.append(int(sys.stdin.readline()))
max_left,max_right, left, Right = trophy[0],trophy[-1], 1, 1
#왼쪽에서 
for i in range(1,N):
    if trophy[i] > max_left:
        left +=1
        max_left = trophy[i]
    else:
        continue
#오른쪽으로
for i in range(N-1,-1,-1):
    if max_right < trophy[i]:
        Right +=1
        max_right = trophy[i]
    else: 
        continue
print(left)
print(Right)