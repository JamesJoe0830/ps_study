# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 87946. 피로도 [🥈 LEVEL 2]
# 📚 알고리즘 분류: Brute Force
# ⏰ 걸린 시간 : 21분
# 
# [풀이 방법]
# 0. permutations (순열)을 사용해서 모든 방법을 다 구해서
# 1. 각각을 방문해서 '최소 필요 피로도'값을 비교해서 '소모 필로도'값을 제거하면서 계산해나간다.
# 2. 이때 cnt값을 올린후에 answer의 값으로 비교해서 더 크다면 update한다.
# ----------------------------------------------------------------------------

import itertools
def solution(k, dungeons):
    answer = 0
    permu = list(itertools.permutations(dungeons,len(dungeons)))
    for dungeons in permu:
        cnt = 0
        fatigue = k
        for need_min, use_fatigue in dungeons:
            if fatigue >= need_min and fatigue >=use_fatigue:
                fatigue -= use_fatigue
                cnt +=1
        answer = max(cnt, answer)
            
    return answer

# ----------------------------------------------------------------------------
# recursion DFS를 사용한 풀이
answer = 0

def dfs(k, cnt, dungeons, visited):
    global answer 
    if cnt > answer:
        answer = cnt
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False
        
def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer