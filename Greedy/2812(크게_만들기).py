#  https://www.acmicpc.net/problem/2812 (골드3) =>오답필요(패캠 강의 참조함) 좋은문제
# <stack 의 개념을 사용하는 정말 좋은 문제>
# 
# Greedy 
# <접근 방법>
# 0. stack을 이용해서 pop append 해줌  
# 1. #스택이 비어있지 않고 현재 원소가 스택의 top보다 크다면 계속해서 꺼내주면 된다.
# 2. stack (LIFO)
# -----------------------------------------------------------------------------

import sys
input = sys.stdin.readline

N, K = map(int,input().split())
Num = (input()).rstrip()
count = 0 #제거 되는 개수
stack = []

for i in Num:
    while len(stack)> 0 and stack[-1] <i: #스택이 비어있지 않고 현재 원소가 스택의 top보다 크다면 계속해서 꺼내주면 된다.
        if count == K:
            break
        else:
            stack.pop() # 계속 빼줌
            count += 1
    stack.append(i)

if count != K : # 위에서 for 문을 다 돌고 41777777 이런경우에는 41만 빠졌을 것이므로 더빼줌
    for i in range(K-count):
        stack.pop() # 뒤에서 빠짐
print(''.join(stack))

# -----------------------------------------------------------------------------

# [풀이방법 0]----------------------------------------------------------------------
# 아래는 코드는 시간초과 뜸
# Greedy 
# <접근 방법>
# 0. 가장 큰수를 저장하는데 앞에서 부터 검사하고 (숫자길이-자리수를 해서 그만큼만 for문을 돌린다.) 

# max_value = int(Num_list[0]) #max_value는 
# max_index, count, answer = 0, 0, '' #max_index : 앞에서 최고값의 인덱스 추출 #count 는 pop의 개수가 4개인 것을 확인하기 위함 
# for i in range(1,N-K):
#     if int(Num_list[i]) > max_value:
#         max_value = int(Num_list[i])
#         max_index = i
#         count =max_index

# for i in range(max_index):
#     Num_list.pop(0)

# if count !=K:
#     for i in range(1,len(Num_list)-1):
#             if count !=K and int(Num_list[i-1])>= int(Num_list[i]) and int(Num_list[i]) <= int(Num_list[i+1]):
#                 Num_list.pop(i)
#                 count+=1
#             if count ==K:
#                  print(''.join(Num_list))
# -----------------------------------------------------------------------------
