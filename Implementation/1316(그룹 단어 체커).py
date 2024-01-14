# https://www.acmicpc.net/problem/1316
# 1316.그룹 단어 체커 [🥈 실버 4]
# 📚 알고리즘 분류: 구현, 문자열
# ⏰ 걸린 시간 : 5분
#
# [문제 풀이]
# 0. 문자열 입력 받으면 그때 마다 체크 함수로 이동
# 1. 체크함수에서 중복 배열에 있는지 먼저 검사하고
# 2. 중복배열이 있다면 바로 이전의 값이랑 연속되는지 확인하기 위해서 distinc[-1]과 같으면 continue
# 3. 그렇지 않다면 0을 반환하게 한다.
# ------------------------------------------
import sys

N = int(input())


def check(str):
    distinc = []
    for s in str:
        if s not in distinc:
            distinc.append(s)
        else:
            if s == distinc[-1]:
                continue
            else:
                return 0
    return 1


cnt = 0
for i in range(N):
    str = input()
    if check(str):
        cnt += 1
print(cnt)
# ------------------------------------------
