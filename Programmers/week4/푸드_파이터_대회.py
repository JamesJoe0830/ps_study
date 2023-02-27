def solution(food):
    answer = ''
    food_len=0
    # for i in range(0,len(food)):
    #     if i != 0:
    #         food[i] = food[i]-food[i]%2
    #     food_len += food[i]
    #     print(food_len)
    for j in range(1,len(food)):
        answer += str(j)*(food[j]//2)
    answer =answer+'0'+ ''.join(reversed(list(answer)))
    return answer