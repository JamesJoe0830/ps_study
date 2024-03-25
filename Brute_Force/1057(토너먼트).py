# https://www.acmicpc.net/problem/1057
# 1057. 토너먼트 [🥈 실버4]
# 📚 알고리즘 분류: 브루트 포스 [Brute Force 알고리즘]
# ⏰ 걸린 시간 : 30분 -> 🔥 오답 필요 (떠오르지 않아서 참고함)
# 
# [문제 풀이]
# 0. jimin이 이기고 다음으로 올라가면 jimin - jimin//2의 값인 번호 갖고 올라간다.
# 1. 수학적으로 접근하면 위와 같은 논리로 결국 Jimin과 hansu가 만나게 된다.
# ----------------------------------------------------------------
import sys
input = sys.stdin.readline

N, jimin, hansu = map (int,input().split())

cnt = 0

while jimin != hansu:
    jimin -= jimin //2
    hansu -= hansu //2 
    cnt +=1
print(cnt)