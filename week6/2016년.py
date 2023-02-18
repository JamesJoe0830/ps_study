# >>> import calendar
# >>> calendar.monthrange(2002,1)
# (1, 31)
def solution(a, b):
    import calendar
    answer = ''
    d_day = ['FRI','SAT','SUN','MON','TUE','WED','THU',]
    t_date = b
    if a==1 :
        t_date = t_date
    else: 
        for i in range(1,a):
            t_date = t_date+ calendar.monthrange(2016,i)[1]
    for j in range(len(d_day)):
        if t_date % 7 == j:
            answer =  d_day[j-1]
    return answer