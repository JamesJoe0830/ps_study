# https://www.acmicpc.net/problem/14502 -> 연구소(골드 4) BFS & DFS
#  <주의 사항>
# 0. 3개의 벽만 설치가 가능하다
# 1. 최소의 바이러스 감염지역을 만들 것
#  ------------------------------------------------------------
import sys
input = sys.stdin.readline 

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
print(graph)

