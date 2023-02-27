def solution(lottos, win_nums):
    answer = []
    eql, cnt=0, 0
    cnt = lottos.count(0) #알수 없는 번호인 0의 개수 추출
    rank = {6 : 1, 5 :2, 4:3, 3:4, 2:5, 1:6, 0:6} #당첨내용에 따른 순위
    
    for i in range(len(lottos)):
            for j in range(len(win_nums)):
                if lottos[i] == win_nums[j]:
                    eql +=1
    if cnt ==0 :
        answer.append(rank[eql])
        answer.append(rank[eql])
    elif cnt !=0:
        answer.append(rank[eql+cnt])
        answer.append(rank[eql])
    return answer