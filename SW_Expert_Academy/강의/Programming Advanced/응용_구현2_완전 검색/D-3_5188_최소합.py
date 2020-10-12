'''
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
1 2 3
2 3 4
3 4 5
그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13

출력
#1 15
#2 18
#3 33
'''
import  sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Advanced/응용_구현2_완전 검색/5188_최소합.txt", "r")
dy,dx = [1,0],[0,1]
def  minLength(Y,X,Sum):
    global minSum
    if Sum > minSum:
        return
    Sum +=  Field[Y][X]
    for i in range(2):
        tempY,tempX = Y+dy[i],X+dx[i]
        if tempY in range(N) and tempX in range(N):
            minLength(tempY,tempX,Sum)
    if Y == N-1 and X == N-1:
        if Sum < minSum:
            minSum = Sum
    return minSum 

for tc in range(1,int(sys.stdin.readline())+1):
    N = int(sys.stdin.readline())
    Field = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
    minSum = 10*N*N
    minSum = minLength(0,0,0)
    print('#%d'%tc,minSum)]

for tc in range(1,int(input())+1):
    N = int(input())
    Field = [list(map(int,input().split())) for _ in range(N)]
    minSum = 10*(2*N-1)
    minSum = minLength(0,0,0)
    print('#%d'%tc,minSum)