import heapq
import sys

N = int(sys.stdin.readline())
heap=list()

for i in range(0,N):
    x= int(sys.stdin.readline())
    if x==0:
      if not heap:
        print(0)
      else:
        print(abs(heapq.heappop(heap))) # heappop은 최소값 추출 
    else :
        heapq.heappush(heap,-x) # 최대값을 추출해주기 위해 -x 값들을 힙에 넣어주고 추출할때 절대값씌워주자
