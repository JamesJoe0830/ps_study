# https://www.acmicpc.net/problem/20365 -> 블로그(실버 3) -> Greedy -> 오답필요
# ---------[딕셔너리 사용한 좋은문제] ----------------------------------------------
# <Greedy 인 이유 ?>
# 0. 칠하는 경우의 수 중 '최소로 칠하는 경우의 수'를 원함
# 
# <문제 푸는 방법>
# 0. 파란색과 빨간색의 개수가 많은 것을 체크할 것
# 1. 바뀌는 것을 flag 를 통해 개수 cnt 해줄 것
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

N = int(input())
Blog_str = input().strip()
Blog = []
answer = 0
# dictionary 사용 -> 오답 해야할 부분
cnt = {'B': 0, 'R': 0}

for i in Blog_str:
    Blog.append(i)
cnt[Blog[0]] +=1  # 첫 색칠 해놓는 것
for i in range(1,N):
    if Blog[i] != Blog[i-1]:
        cnt[Blog[i]] +=1
answer = min(cnt['B'],cnt['R']) + 1 
# +1 은 더 많은것 먼저 전체 칠하는것 
print(answer)


# -----------------------------------------------------------------------------
# [풀이방법 1]--------------------------------------------------------------------
# import sys
# input = sys.stdin.readline

# N = int(input())
# Blog_str = input().strip()
# Blog = []
# cnt = 1

# for i in Blog_str:
#     Blog.append(i)

# for i in range(len(Blog)-1, 0, -1):
#     if Blog[i] == Blog[i-1]:
#         Blog.pop(i)


# B_cnt = Blog.count("B")
# R_cnt = Blog.count("R")



# # B의 개수가 많을떄 
# if B_cnt >= R_cnt:
#     if Blog[0] != "B":
#         cnt += 1
#     for i in range(1,len(Blog)):
#         if Blog[i] =="R" and Blog[i] != Blog[i-1]:
#             cnt+=1 
        
# # R의 개수가 많을때 
# if B_cnt < R_cnt: 
#     if Blog[0] != "R":
#         cnt +=1 
#     for i in range(len(Blog)):
#         if Blog[i] =="B" and Blog[i] != Blog[i-1]:
#             cnt +=1
# print(cnt)
#  -----------------------------------------------------------------------------
# 
# [풀이방법 0]--------------------------------------------------------------------
# 아래의 경우에는 RBBBR이나 RBBRBBR 같은 예외 case를 고려하고 있지 않다.
# ->해결책 : 연속해서 같은게 나타나면 0같은 것으로 대체한다. 

# import sys
# input = sys.stdin.readline

# N = int(input())
# Blog_str = input().strip()
# Blog = []
# cnt = 1

# for i in Blog_str:
#     Blog.append(i)
# B_cnt = Blog.count("B")
# R_cnt = Blog.count("R")
# print(Blog)


# # B의 개수가 많을떄 
# if B_cnt >= R_cnt:
#     if Blog[0] != "B":
#         cnt += 1
#     for i in range(1,N):
#         if Blog[i] =="R" and Blog[i] != Blog[i-1]:
#             cnt+=1 
        
# # R의 개수가 많을때 
# if B_cnt < R_cnt: 
#     if Blog[0] != "R":
#         cnt +=1 
#     for i in range(N):
#         if Blog[i] =="B" and Blog[i] != Blog[i-1]:
#             cnt +=1
# print(cnt)