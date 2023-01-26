def solution(x):
    answer = True
    str_x =str(x)
    list_x=list(str_x)
    sum_x =0
    for i in range(len(str_x)):
        sum_x += int(list_x[i])
    if x%sum_x ==0:
        answer=True
    elif x%sum_x != 0:
        answer=False
    return answer