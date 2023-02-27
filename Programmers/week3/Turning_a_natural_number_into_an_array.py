def solution(n):
    answer = []
    str_n = str(n)
    list_n = list(str_n)
    for x in range(len(str_n)):
        answer.append(int(list_n[len(str_n)-1-x]))
    return answer