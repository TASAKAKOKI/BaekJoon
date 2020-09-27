'''
N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 N과 M이 주어지고, 다음 줄에 10억 이하의 자연수 N개가 주어진다. 3<=N<=20, N<=M<=1000,

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.
 
입력
3
3 10
5527 731 31274
5 12
18140 14618 18641 22536 23097
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907	 

출력
#1 731
#2 18641
#3 2412
'''

# 0 using sys.stdin
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Queue1/input_5097.txt", "r")
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