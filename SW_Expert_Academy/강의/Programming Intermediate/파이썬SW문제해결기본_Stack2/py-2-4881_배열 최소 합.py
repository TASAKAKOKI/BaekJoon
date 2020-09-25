'''
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
예를 들어 다음과 같이 배열이 주어진다.
2 1 2
5 8 5
7 2 2
이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.

입력
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8	 

출력
#1 8
#2 14
#3 9
'''

# 0 using sys.stdin
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Stack2/input_4881.txt", "r")
def findMinSum(row,tempSum):
    global minSum
    if tempSum > minSum:
        return minSum
    if row == N:
        if tempSum < minSum:
            minSum = tempSum
        return minSum
    for i in range(N):
        if not visitedRow[i]:
            visitedRow[i] = 1
            findMinSum(row+1,tempSum+metrix[i][row])
            visitedRow[i] = 0
    return minSum

T = sys.stdin.readline()
for tc in range(1, int(T)+1):
    N = int(sys.stdin.readline().strip())
    metrix = [list(map(int,sys.stdin.readline().strip().split())) for i in range(N)]
    visitedRow = [0]*N
    minSum = (N*9)+1
    findMinSum(0,0)
    print(f'#{tc} {minSum}')

# 1 using input
def findMinSum(row,tempSum):
    global minSum
    if tempSum > minSum:
        return minSum
    if row == N:
        if tempSum < minSum:
            minSum = tempSum
        return minSum
    for i in range(N):
        if not visitedRow[i]:
            visitedRow[i] = 1
            findMinSum(row+1,tempSum+metrix[i][row])
            visitedRow[i] = 0
    return minSum
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    metrix = [list(map(int,input().split())) for i in range(N)]
    visitedRow = [0]*N
    minSum = (N*9)+1
    findMinSum(0,0)
    print(f'#{tc} {minSum}')