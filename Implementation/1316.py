# https://www.acmicpc.net/problem/1316
# 1316.그룹 단어 체커 [🥈 실버 5]
# 📚 알고리즘 분류: 구현, 문자열
# ⏰ 걸린 시간 : 3분
#
# [문제 풀이]
# 0. 문자열 입력 받으면 그때 마다 체크 함수로 이동
# 1. 체크함수에서 중복 배열에 있는지 먼저 검사하고
# 2. 중복배열이 있다면 바로 이전의 값이랑 연속되는지 확인하기 위해서 stack[-1]과 같으면 continue
# 3. 그렇지 않다면 0을 반환하게 한다.
# -------------------------------------------------------------------------------

import sys
input = sys.stdin.readline
N = int(input())

answer = 0
for t in range(N):
  word = input()
  stack = []
  answer +=1 
  for w in word:
    if w not in stack:
      stack.append(w)
    else:
      if stack[-1] != w :
        answer -= 1
        break
      else :
        stack.append(w)

print(answer)

# -------------------------------------------------------------------------------