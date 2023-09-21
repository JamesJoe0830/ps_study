# https://www.acmicpc.net/problem/10828
# 10828. 스택 [🥈 실버 4]
# ⏰ 걸린시간 : 10분
# 
# [주의사항]
# input 받을때 \n이 있으므로 rstrip해줄것
# 
# [문제풀이]
# deque을 통해서 stack을 구현
# stack은 LIFO(Last In First Out)이다.
# ------------------------------------------------

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
stack1 = deque()
for i in range(N):
    cmd = input().strip()
    if cmd.split()[0] == 'push':
        stack1.append((int(cmd.split()[1])))
    elif cmd == 'pop':
        if len(stack1) > 0:
            answer = stack1.pop()
        else:
            answer = -1
        print(answer)
    elif cmd == 'size':
        print(len(stack1))
    elif cmd == 'empty':
        if len(stack1) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(stack1) > 0:
            answer = stack1[-1]
        else:
            answer = -1
        print(answer)
# ------------------------------------------------