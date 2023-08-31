# https://level.goorm.io/exam/195693/%ED%86%B5%EC%A6%9D-2/quiz/1
import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int,input().split())
answer = int(1e9)
X = N // B # 큰값의 몫
dN = N % B
Y = dN // A

def MinAns(N,A,B,X,Y,dN):
    global answer 
    while X>=0:
        if X * B + Y * A == N:
            answer =X+Y
            return answer
        else:
            X -=1
            dN = N - (B * X)
            Y = dN //A
    return answer
answer = MinAns(N, A, B, X, Y,dN)

if answer != int(1e9):
    print(answer)
else:
    print(-1)
