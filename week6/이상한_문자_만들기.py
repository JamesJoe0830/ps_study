def solution(s):
    answer = []
    arr=[]
    s_list = s.split(" ")
    print(s_list)
    for i in range(len(s_list)):
        for j in range(len(s_list[i])):
            if j % 2 ==0:
                arr.append(s_list[i][j].upper())
            else:
                arr.append(s_list[i][j].lower())
        arr.append(' ')
    arr=''.join(arr)
    print(arr)
    answer=arr[0:len(arr)-1]
    return answer