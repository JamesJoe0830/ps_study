N = int(input())
# T: 시간 M : 분

T, M = map(int,input().split())
Times=0
Hour, Min = 0, 0
for i in range(N):
	task_time = int(input())
	Times += task_time
Hour = Times // 60 
Min = Times % 60

T = T + Hour 
M = M + Min
if M >= 60:
	T +=1
	M -= 60 

print(T % 24, M)