# https://www.acmicpc.net/problem/2875 => (브론즈 3) 대회 or 인턴
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())	# n 여학생 수, m 남학생 수, k 인턴쉽 학생 수
Team = 0
  # 대회나갈 팀
# K ==0 or K != 0 일때로 나누기
# 남자가 많을경우 여자가 많을경우 나누기
# 여자 남자 2대 1 비율

while N >= 2 and M >= 1 and N + M >= K + 3:	# 2명 , 1명 팀 만들 수 있고, 인턴쉽도 보낼 수 있는 수 일때
    N -= 2	# 빼주고
    M -= 1	# 빼주고
    Team += 1	# 팀 수는 하나씩 더해준다
print(Team)



# if K == 0 :
#     Team= min(woman //2, man)

# elif K !=0:
#     if woman > man:
#         Team = (woman+man - K) // 3
#     if woman <= man:
#         if man - woman//2  >= K:
#             Team = M // 2
#         elif M- M//2 <K:
#             Team = (woman+man - K) // 3
# elif M+M <= K:
#     Team = 0
