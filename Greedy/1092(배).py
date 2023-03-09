import sys
input = sys.stdin.readline
N = int(input()) # 크레인 대수
cranes= list(map(int,(input().split())))# 각 크레인의 무게 제한
M = int(input()) # 박스의 수 
boxs= list(map(int,(input().split())))         # 각 박스의 무게
# print(box)

cranes.sort(reverse=True)
boxs.sort(reverse=True)


if cranes[0] < boxs[0]: #무게가 애초에 크레인보다 큰경우에는 모든박스를 옮길 수 없는 경우임
    print(-1)
    sys.exit()
else:
    time =0

    while boxs: # crane을 계속해서 돌게 해야함 box가 없어질때 까지
        if not boxs:
            break

        for crane in cranes:
            for box in boxs:
                if crane >= box:
                    boxs.remove(box) #해당하는 박스 제거해주기
                    break
        time +=1  # 한싸이클 돌때 시간 측정 (크레인은 동시에 일하므로)

print(time)
