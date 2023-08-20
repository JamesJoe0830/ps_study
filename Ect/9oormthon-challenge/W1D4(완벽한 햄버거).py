def check(N,burger,max_index):
	Perfect = True
	for i in range(max_index,N-1):
		if burger[i] < burger[i+1]:
			Perfect = False

	for i in range(max_index,0):
		if burger[i] < burger[i-1]:
			Perfect = False
			
	return Perfect
	
N = int(input())
burger = list(map(int,input().split()))
max_index= burger.index(max(burger))


if check(N,burger,max_index) == True:
    print(sum(burger))
elif check(N,burger,max_index) == False:
	print(0)
