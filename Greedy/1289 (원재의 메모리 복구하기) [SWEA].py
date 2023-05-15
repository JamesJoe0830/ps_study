# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 1289. 원재의 메모리 복구하기 [D3]
# 
# < 🔍 Greedy인 이유? >
# 0. 문제에서 초기값에서 원래값으로 복구하기 위한 최소 수정 횟수를 출력하는 것임으로
# 
# < 💡 문제 풀때 핵심 포인트>
# 0. 결국엔 메모리를 초기값에서 원상복구 하는 것은  == 원상복구 상태에서 초기값으로 설정하는 것과 같다.
#  -> So 나는 원상복구에서 초기값으로 변경해버림 
#
# ------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

T = int(input())
answer = []


def check(memory):
    global answer
    cnt = 0
    i = 0
    for i in range(len(memory)):
        if memory[i] == '1':
            cnt+=1
            for j in range(i, len(memory)):
                if memory[j] == '1':
                    memory[j] = '0'
                elif memory[j] == '0':
                    memory[j] = '1'
    answer.append(cnt)



for test_case in range(T):
    memory = list(input().rstrip())
    check(memory)


# 출력
for i in range(T):
    print('#{} {}'.format(i+1,answer[i]))
# ------------------------------------------------------------------------------

