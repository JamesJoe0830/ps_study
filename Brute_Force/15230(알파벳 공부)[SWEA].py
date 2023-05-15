# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYLnMQT6vPADFATf&categoryId=AYLnMQT6vPADFATf&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 15230. 알파벳 공부[D3]
#
#
#
#
#
# -----------------------------------------------------------------------------

TC = int(input())

Alpha = "abcdefghijklmnopqrstuvwxyz"
answer = []


def Compare(test):
    cnt = 0
    for i in range(len(test)):
        if Alpha[i] == test[i]:
            cnt += 1
        else:
            break

    answer.append(cnt)


for test_case in range(TC):
    test_Alpha = input()
    Compare(test_Alpha)
# 출력
for i in range(TC):
    print("#{} {}".format(i+1, answer[i]))
# -----------------------------------------------------------------------------

