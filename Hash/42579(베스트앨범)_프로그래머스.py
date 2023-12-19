# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 42579. 베스트앨범 [🥈 LEVEL 3] - 오답 필요
# 📚 알고리즘 분류: 해쉬
# ⏰ 걸린 시간 : 63분
# 시간 복잡도 : O(n*m) m은 장르 개수
# [문제 풀이]
# 0. cnt 딕셔너리로 모든 장르별 총 재생회수를 구한다. 먼저 들어가야할 우선순위를 정해주기 위함
# 1. song 딕셔너리를 통해 원래 index값과 genres, plays 를 함께 저장한다.
# 2. 각 장르별로 최대 2개씩만 넣을 것이기 때문에 cnt_num을 2보다 작을때만 설정해준다.
# 3. 넣을때 마다 cnt_num을 +1씩 올려준다.
# ----------------------------------------------------------------------------
def solution(genres, plays):
    answer = []
    n = len(genres)
    #cnt 는 제일 많이 재생된 장르를 내림차순으로 갖고 있는 dict
    cnt = dict()
    # song 은 index : (genres[i],plays[i]) 이렇게 이뤄진 dict
    song = dict()
    # 장르별 횟수
    for i in range(n):
        song.update({i:(genres[i],plays[i])})
        if genres[i] not in cnt:
            cnt.update({genres[i]:plays[i]})
        else:
            cnt[genres[i]] += plays[i]
    cnt = dict(sorted(cnt.items(), key = lambda item : item[1],reverse =True))
    song = dict(sorted(song.items(),key =lambda item : item[1], reverse = True))
    
    # 두개씩 만 넣기 위해서 cnt_num을 2보다 작을때 넣어줌
    for i in cnt:
        cnt_num = 0
        for key in song :
            if i == song[key][0] and cnt_num < 2:
                cnt_num+=1
                answer.append(key)
            
    return answer
# ----------------------------------------------------------------------------