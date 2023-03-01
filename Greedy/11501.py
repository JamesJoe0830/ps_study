import sys
answer = [] 
T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    buy, earn, cnt = 0, 0, 0
  
    for i in range(len(a)-1):
        if a[i]<=a[i+1]:
            buy += 1*a[i]
            cnt +=1
        elif a[i]>a[i+1]:
            earn += cnt*a[i] - buy
            cnt=0
            buy =0
    if buy != 0:
        earn = earn + cnt*a[len(a)-1]-buy
    answer.append(earn)
for i in answer:
    print(i)
