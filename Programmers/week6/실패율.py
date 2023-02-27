# len(stages)-이게 현재 도전 사람수 stages[i] == i+1 이때 count 이게 1에서 머무르고 있는 사람
# if 문으로 확률을 각각 배열에 배치하고 실패율 내림차순
# 위의 if문에 만일 확률이 같다면 작은 스테이지부터 배열
# N이 스테이지 수
def solution(N, stages):
    answer = []
    dic = {}
    nop = len(stages) 
    for i in range(1,N+1):
            if stages.count(i) != 0:
                dic[i] = stages.count(i) / nop
                nop = nop -stages.count(i)
            else:
                dic[i]=0
    dic=sorted(dic.items(),key = lambda item:item[1],reverse=True)
    for j in dic:
        answer.append(j[0])
    return answer