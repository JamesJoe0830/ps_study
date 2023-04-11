# https://www.acmicpc.net/problem/4796 => 캠핑 (브론즈1) 
# <풀이방법>
# 0. 전체 휴가일수 V / 연속하는 P일 수 -> 몫과 나머지을 구한다.
# 1. 몫 x 시용가능한 L일 + 나머지일 수 
# <주의사항>
# -> 남머지가 사용일수보다 클경우는 사용일수가 더해지도록 하는게 포인트이다.
# -----------------------------------------------------------------------------------------
import sys 
input = sys.stdin.readline
answerList = []
answer= 0
while True:
    L, P, V = map(int,input().split())

    if L + P + V == 0 :
        break
    Quo = V // P #Quotient (몫)
    remain = min(V % P,L) #remainder (나머지) 
    #이게 포인트인데 3 9 17 이거는 사용가능한 일수가 나머지보다 더 작으므로 min을 활용해야한다.

    answer = Quo * L + remain
    answerList.append(answer)

# 출력
for i in range(len(answerList)):
    print("Case %d: %d"%(i+1,answerList[i]))
# -----------------------------------------------------------------------------------------

