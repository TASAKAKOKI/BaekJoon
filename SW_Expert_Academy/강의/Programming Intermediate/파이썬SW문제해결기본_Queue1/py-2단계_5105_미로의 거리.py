'''
NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

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
#1 5
#2 5
#3 0
'''

# 0 using sys.stdin
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Queue1/input_5105.txt", "r")

dy,dx = [-1,0,1,0],[0,1,0,-1]
            
def BFS():
    global Q
    distance = 0
    while Q:
        sameLevelNodes = []
        while Q:
            Y,X = Q.pop(0)
            # 방문하면, visited[Y][X] 를 1로 변경
            if not visited[Y][X]:
                visited[Y][X] = 1
                for i in range(4):
                    tY,tX = Y + dy[i], X +dx[i]
                    if tY in range(N) and tX in range(N):
                        if Maze[tY][tX] == 0:
                            sameLevelNodes.append((tY,tX))
                        elif Maze[tY][tX] == 3:
                            return distance
        Q = sameLevelNodes
        distance += 1
    return 0        

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    Maze = [list(map(int,list(sys.stdin.readline().strip()))) for i in range(N)]
    Q = []
    # print(Maze)
    for i in range(N):
        if 2 in Maze[i]:
            Q.append((i,Maze[i].index(2)))
            break
        else: continue
    visited = [[0]*N for _ in range(N)]
    # print(visited)
    minLen = BFS()
    print(f'#{tc} {minLen}')

# 1 using input
dy,dx = [-1,0,1,0],[0,1,0,-1]
            
def BFS():
    global Q
    distance = 0
    while Q:
        sameLevelNodes = []
        while Q:
            Y,X = Q.pop(0)
            # 방문하면, visited[Y][X] 를 1로 변경
            if not visited[Y][X]:
                visited[Y][X] = 1
                for i in range(4):
                    tY,tX = Y + dy[i], X +dx[i]
                    if tY in range(N) and tX in range(N):
                        if Maze[tY][tX] == 0:
                            sameLevelNodes.append((tY,tX))
                        elif Maze[tY][tX] == 3:
                            return distance
        Q = sameLevelNodes
        distance += 1
    return 0        

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Maze = [list(map(int,list(input()))) for i in range(N)]
    Q = []
    # print(Maze)
    for i in range(N):
        if 2 in Maze[i]:
            Q.append((i,Maze[i].index(2)))
            break
        else: continue
    visited = [[0]*N for _ in range(N)]
    # print(visited)
    minLen = BFS()
    print(f'#{tc} {minLen}')