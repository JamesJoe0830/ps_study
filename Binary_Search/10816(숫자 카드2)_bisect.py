# https://www.acmicpc.net/problem/10816
# 10816.숫자 카드 2 [🥈 실버 4]
# 📚 알고리즘 분류: 이진 탐색
# ⏰ 걸린 시간 : 20분
#
# [시간 초과 해결방법]
# 0. 처음에 일치하는 mid값을 찾으면 왼쪽 오른쪽으로 while문을 돌려서 카운트 해주는 방식이에서 시간초과 발생
# 1. bisect 이진탐색 라이브러리로 해결
# 2. bisect_left 해당 값 맨왼쪽 인덱스 찾아줌
# 3. bisect_right 해당 값 맨오른쪽 인덱스 찾아줌
# ✨ bisect 이진탐색 인덱스 값 찾아주는거 유용하다.
# [이진 탐색인 근거]
# 0. M개의 값중 N개를 탐색하는 것은 최악의 경우 250,000,000,000 ->  2500초가 걸린다.
# 1. 탐색을 브루트 포스로 하면 안되고 이진 탐색으로 시간복잡도를 낮춰야한다.(logN)
# --------------------------------------------------------------------------------
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
have_card = list(map(int,input().split()))
M = int(input())
guess_card = list(map(int,input().split()))
answer = []

have_card.sort()
for i in range(M):
    cnt = 0 
    start = 0
    end = N-1
    now = guess_card[i]
    cnt = bisect_right(have_card,now) - bisect_left(have_card,now)
    answer.append(cnt)
print(*answer)
# --------------------------------------------------------------------------------