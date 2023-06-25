import sys
# import time
# start_time = time.time()

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
A.sort()



for i in range(N):
    start = 0
    end = N-1
    if B[i]< A[0] or B[i] > A[N-1]: # 초기에 벗어나는 범위는 0으로 출력
        print(0)
    else:
        while start <= end:
            mid = (start+ end) //2
            if B[i] == A[mid]:
                print(1)
                break
            elif B[i] > A[mid]:
                start = mid +1
            elif B[i] < A[mid]:
                end = mid -1
            # if start == end and B[i]!= A[mid]:
            #         print(0)
            #         break

        # if A[start] <= B[i]<=A[mid]:
        #     end = mid 
        #     mid = (mid //2)
        #     if mid == end and A[end] == B[i]:
        #         print(1)
        #         break
        # if A[mid] < B[i] <=A[end]:
        #     start = mid+1 
        #     mid = (end +start) // 2
        #     if mid == end :
        #         print(1)
        #         break
        # elif B[i]> A[end]:
        #     print(0)
            # break

# end_time = time.time()

# print(end_time - start_time)