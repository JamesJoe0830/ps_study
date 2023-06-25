# https://www.acmicpc.net/problem/2212 -> 센서(꼴드 5)

import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
Sensors=list(map(int,input().split())) # 센서 리스트 
Sensors.sort()
print(Sensors)