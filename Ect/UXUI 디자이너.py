# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# N : 이벤트 개수, M : 사용자의 수, k = i번째 사용자가 실행한 이벤트의 개수 
N, M = map(int,input().split())
counts=[0]*N
answer = []
for i in range(M):
	row = input().split()
	k = int(row[0])
	events = list(map(int,row[1:]))
	for event in events:
		counts[event-1] +=1

max_count = max(counts)
for i in range(N):
	if counts[i]  == max_count:
		answer.append(i+1)
answer.sort(reverse=True)

print(*answer)

