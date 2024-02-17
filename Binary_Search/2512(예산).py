# https://www.acmicpc.net/problem/2512
# 2512. 예산 [🥈 실버 2] -> 🔥 오답 필요
# 📚 알고리즘 분류: 이진 탐색(Binary Search)
# ⏰ 걸린 시간 : 35분
#
#
# [풀이 방법]
# 0. 이진 탐색을 통해서 O(logN)의 시간복잡도를 갖고 문제를 접근한다.
# 1. 만일 모든 값의 합이 총 금액 넘지 않으면 바로 지역의 최대 예산 값 출력한다.
# 2. 그렇지 않으면 계속해서 더하지만 mid의 값을 업데이트 해준다.
# ------------------------------------------------------------------------
import sys
input = sys.stdin.readline

N = int(input())
# 각 지역의 예산
moneys = list(map(int, input().split()))
moneys.sort()
# 국가예산 총 금액
budgets = int(input())

if sum(moneys) <= budgets:
    print(moneys[-1])
else:
    allowment = budgets // N
    start = 0
    end = moneys[N-1]
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in moneys:
            if i > mid:
                total += mid
            else:
                total += i
        if total <= budgets:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
# ------------------------------------------------------------------------
