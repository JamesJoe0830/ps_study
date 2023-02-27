import sys
N = int(sys.stdin.readline())
arr= [[ 0 for j in range(N)] for i in range(N)]
#for k in range(N):
    # arr row[0]에 1개 col에 값이 입력되면 row[1]로 넘어감
    # row [1]에서는 row[0]에서 입력된 같은 col은 전부 제외 / 대각선의 위치해 있는 것도 제외
    # row [2]에서는 row[0]과 row[1]에서 입력된 값이 위치한 col은 제외 하고 / 대각선의 위치한 것도 제외
    # 위와 같은 로직을 반복해서 가능한 조합의 개수 추출  
print(arr)