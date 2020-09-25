'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

입력
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000	 

출력
#1 1
#2 1
#3 0
'''

'''
# 0 using sys.stdin
def isRange(Y,X):
    return 1 if X in range(N) and Y in range(N) else 0
def isVisited(Y,X):
    return 1 if [Y,X] in visited else 0
def inStack(Y,X):
    return 1 if [Y,X] in stack else 0
def canGo(Y,X):
    return 1 if Maze[Y][X] == 0 or Maze[Y][X] == 2 else 0
def isWall(Y,X):
    return 1 if Maze[Y][X] == 1 else 0
def isGoal(Y,X):
    return 1 if Maze[Y][X] == 3 else 0

def backtrack(Y,X):
    global result
    stack.append([Y,X])
    for k in range(4):
        if result == 1:
            break
        tY,tX = Y+dy[k],X+dx[k]
        if not isRange(tY,tX) or isWall(tY,tX) or inStack(tY,tX) or isVisited(tY,tX):
            continue
        elif isGoal(tY,tX):
            print(Maze[tY][tX])
            print('found!')
            result = 1
            break
        else:
            print('can go?:',canGo(tY,tX))
            backtrack(Y+dy[k],X+dx[k])
    if result == 1:
        return 1
    elif len(stack) != 0:
        visited.append(stack.pop())
        if len(stack) != 0:
            Y,X = stack.pop()
            backtrack(Y,X)
        else:
            print('nothing more left')
            result = 0
            return 0
    else:
        print('nothing more left')
        result = 0
        return 0

import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Stack2/input_4875.txt", "r")
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    result = -1
    N = int(sys.stdin.readline())
    Maze = [sys.stdin.readline().strip() for i in range(N)]
    Y,X = 0,0
    for i in range(N):
        if '2' in Maze[i]:
            Y,X = i, Maze[i].index('2')
        Maze[i] = list(map(int,Maze[i]))
    stack = []
    visited = []
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    print('initial Y, X is:',Y,X)
    while result == -1:
        r = backtrack(Y,X)
    print('#%d %s'%(tc,result))

    # print(f'#{tc} {result}')
'''

'''
# 0-1 import sys 이용
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Stack2/input_4875.txt", "r")

dy = [-1,1,0,0]
dx = [0,0,-1,1]
dir = ['u','d','l','r']

def isRange(Y,X):
    return 1 if X in range(N) and Y in range(N) else 0
def notVisited(Y,X):
    return 0 if [Y,X] in visited else 1
def notWall(Y,X):
    return 0 if Maze[Y][X] == 1 else 1
def isGoal(Y,X):
    return 1 if Maze[Y][X] == 3 else 0
def changeYX(Y,X,D):
    k = dir.index(D)
    return [Y+dy[k],X+dx[k]]
def backtrack(Y,X):
    global result
    if isGoal(Y,X):
        result = 1
        return 1 
    else:
        L = len(stack)
        for i in range(4):
            tY = Y + dy[i]
            tX = X + dx[i]
            if isRange(tY,tX) and notWall(tY,tX) and notVisited(tY,tX):
                stack.append([Y,X,dir[i]])
        if L == len(stack):
            try:
                Y,X,D = stack.pop()
                Y,X = changeYX(Y,X,D)
                backtrack(Y,X)
            except:
                return 0
        else:
            if notVisited(Y,X):
                visited.append([Y,X])
            try:
                Y,X,D = stack.pop()
                Y,X = changeYX(Y,X,D)
                backtrack(Y,X)
            except:
                return 0
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    result = 0
    N = int(sys.stdin.readline())
    Maze = [sys.stdin.readline().strip() for i in range(N)]
    Y,X = -1,-1
    for i in range(N):
        if '2' in Maze[i]:
            Y,X = i, Maze[i].index('2')
        Maze[i] = list(map(int,Maze[i]))
    stack = []
    visited = []
    # print('initial Y, X is:',Y,X)
    backtrack(Y,X)
    print('#%d %s'%(tc,result))
'''

#0 (성공)
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Stack2/input_4875.txt", "r")
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def canGo(Y,X):
    return 1 if Y in range(N) and X in range(N) and Maze[Y][X] != 1 else 0
def findWay(Y,X):
    global result
    if result == 1:
        return 1
    if Maze[Y][X] == 3:
        result = 1
        return 1
    for idx in range(4):
        if result == 1:
            break
        if canGo(Y+dy[idx],X+dx[idx]):
            Maze[Y][X] = 1
            findWay(Y+dy[idx],X+dx[idx])
            Maze[Y][X] = 0
        else:
            continue
    return result

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    Maze = [sys.stdin.readline().strip() for i in range(N)]
    Y,X = 0,0
    for i in range(N):
        if '2' in Maze[i]:
            Y,X = i, Maze[i].index('2')
        Maze[i] = list(map(int,Maze[i]))
    print('initial Y, X is:',Y,X)
    Maze[Y][X] = 1
    result = 0
    findWay(Y,X)
    print('#%d %s'%(tc,result))

# 1 성공 using input()
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def canGo(Y,X):
    return 1 if Y in range(N) and X in range(N) and Maze[Y][X] != 1 else 0
def findWay(Y,X):
    global result
    if result == 1:
        return 1
    if Maze[Y][X] == 3:
        result = 1
        return 1
    for idx in range(4):
        if result == 1:
            break
        if canGo(Y+dy[idx],X+dx[idx]):
            Maze[Y][X] = 1
            findWay(Y+dy[idx],X+dx[idx])
            Maze[Y][X] = 0
        else:
            continue
    return result
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Maze = [input() for i in range(N)]
    Y,X = 0,0
    for i in range(N):
        if '2' in Maze[i]:
            Y,X = i, Maze[i].index('2')
        Maze[i] = list(map(int,Maze[i]))
    print('initial Y, X is:',Y,X)
    Maze[Y][X] = 1
    result = 0
    findWay(Y,X)
    print('#%d %s'%(tc,result))