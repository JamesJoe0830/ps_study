def solution(s):
    answer = True
    list_s=list(s)
    count_p = 0
    count_y = 0
    for x in range(len(s)):
        if list_s[x] == 'p' or list_s[x] =='P':
            count_p += 1
        elif list_s[x] == 'y' or list_s[x] == 'Y':
            count_y += 1
    if count_p == count_y:
        answer = True
    elif count_p != count_y:
        answer = False
    elif count_p + count_y == 0:
        return True
    
    return answer