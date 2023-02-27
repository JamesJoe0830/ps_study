def solution(phone_number):
    answer = []
    listpn =list(str(phone_number))
    
    for x in range(0,len(listpn)-4):
        listpn[x]= '*'
    answer=listpn
    return ''.join(answer)