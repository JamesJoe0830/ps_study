# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    answer = 0
    len_lost = 0
    check = []  # 빌려준 친구들은 제외하기 위한 배열
    for i in range(len(lost)):
        if lost[i] not in reserve:
            len_lost += 1
            for j in range(len(reserve)):
                print("check", i, j, check)
                if reserve[j] not in check and reserve[j] not in lost:
                    if lost[i] - 1 == reserve[j]:
                        check.append(reserve[j])
                        break
                    elif lost[i] + 1 == reserve[j]:
                        check.append(reserve[j])
                        break
    print(len_lost)
    print(check)
    answer = n - len_lost + len(check)
    return answer
