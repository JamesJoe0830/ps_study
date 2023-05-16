# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 1209. [S/W 문제해결 기본] 2일차 - Sum [D3] -> 📝 수학, 📊 그래프
# 
# 
# 
# 
# --------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = 10
row = 100
answer =[]
def Max_sum(graph):
    global answer, row
    sum_arr = []
    # 가로 세로
    for i in range(row):
        sum_x, sum_y =0, 0
        for j in range(row):
            sum_x += graph[i][j] # 가로
            sum_y += graph[j][i] # 세로
            sum_arr.append(sum_x)
            sum_arr.append(sum_y)
    # 대각선         
    sum3, sum4 =0, 0
    # 왼쪽 대각선
    for i in range(row):
        sum3 += graph[(row-1)-i][(row-1)-i]
    sum_arr.append(sum3)
    # 오른쪽 대각선
    for i in range(row):
        sum4 += graph[i][j]
    sum_arr.append(sum4)

    answer.append(max(sum_arr))





for test_case in range(TC):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(row)]
    Max_sum(graph)

for i in range(TC):
    print('#{} {}'.format(i+1,answer[i]))
    
# --------------------------------------------------------------------------------
