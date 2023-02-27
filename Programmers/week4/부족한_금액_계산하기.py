def solution(price, money, count):
    answer = 0
    sum_price=0
    for i in range(count):
        sum_price += price*(i+1)
    if(sum_price > money):
        answer = sum_price - money
    else:
        answer=0
    return answer