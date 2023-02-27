import sys
N= int(sys.stdin.readline())
person,rank = [], []
count =0
answer=''
for i in range(N):
    x, y=map(int,sys.stdin.readline().split())
    person.append([x,y])


for i in range(N):
    count =0
    for j in range(N):
        if person[i][0]< person[j][0] and person[i][1]<person[j][1]:
            count +=1
    rank.append(str(1+count))   
answer=' '.join(rank)
print(answer)
