# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14P0c6AAUCFAYi&categoryId=AV14P0c6AAUCFAYi&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3
# 1213. [S/W 문제해결 기본] 3일차 - String [D3] -> 🧾 문자열
# 
# 
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = 10
answer=[]
def Check(find,sentence,l):
    global answer
    cnt = 0 
    for i in range(0,len(sentence)-1):
        if sentence[i:i+l] == find:
            cnt +=1
    answer.append(cnt)

for test_case in range(TC):
    t = int(input())
    find =input().rstrip()
    sentence = input().rstrip()
    l = len(find)
    Check(find,sentence,l)


for i in range(TC):
    print('#{} {}'.format(i+1, answer[i]))
# -----------------------------------------------------------------------------
