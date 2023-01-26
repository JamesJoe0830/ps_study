def solution(n):
    answer = []
    n_str = str(n)
    n_list = list(n_str)
    k=0
    for x in range(len(n_str)):   
        for y in range(x+1,len(n_str)):
            if int(n_list[x])<int(n_list[y]):
                k = n_list[x] 
                n_list[x]=n_list[y]
                n_list[y]=k
    answer = n_list
    return int(''.join(answer))