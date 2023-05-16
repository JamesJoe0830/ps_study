# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 2805. 농작물 수확하기 [D3] -> 📝 수학, 📊 그래프 
# 
# 마름모 형태의 정사각형 더하는 것
# 
# 
# 
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = int(input())
graph = []
answer =[]


for test_case in range(TC):
    N = int(input())

    graph = [list(map(int,input().rstrip())) for _ in range(N)]
    total = 0 
    for i in range(N):
        if N//2 >= i :
            for j in range(int(N//2)-i,int(N//2)+1+i):
                total += (graph[i][j])

        elif N//2 <i :
            for j in range(int(N//2)-(N-i-1),int(N//2)+(N-i)):
                total += (graph[i][j])

    answer.append(total)


# 출력
for i in range(TC):
    print('#{} {}'.format(i+1,answer[i]))
# -----------------------------------------------------------------------------
