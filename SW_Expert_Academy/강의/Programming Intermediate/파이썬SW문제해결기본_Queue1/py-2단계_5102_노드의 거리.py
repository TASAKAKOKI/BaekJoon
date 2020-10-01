# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
'''
T: 주어질 케이스 수
V: 그래프에는 1번부터V번까지의 노드가 존재
E: 아래에 그래프에 대한 E개의 '방향석이 없는(즉, 양방향 이동 가능)' 간선정보가 주어질 것
S: E개의 간선정보 이후에 주어질 출발노드
G: E개의 간선정보 우히 S와 함께 주어질 도착노드
문제 목표: 주어진 V개의 노드와 E개의 간선정보를 바탕으로 S에서 G까지 이동하는데 필요한 최소 간선의 수
두 노드가 간선으로 연결되어 있지 않은 경우 0 출력
'''



# 실패
'''
def BFS(s,d):
    global minD
    if s == G:
        minD = d
        return minD
    elif d > minD:
        return
    else:
        intS = int(s)-1
        if visited[intS] >= d:
            if Graph[s]:
                for i in range(len(Graph[s])):
                    BFS(Graph[s][i],d+1)
                visited[intS] = d
            else:
                return 0            
        else:
            return    
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Queue1/input_5102.txt", "r")
for tc in range(1, int(sys.stdin.readline())+1):
    V,E = map(int,sys.stdin.readline().strip().split())
    Graph = {str(i):[] for i in range(1,V+1)}
    print(V, Graph)
    for i in range(E):
        s,e = sys.stdin.readline().strip().split()
        if not Graph[s]:
            Graph[s] = [e]
        else:
            Graph[s].append(e)
    print(E, Graph)
    # Queue = []
    S,G = sys.stdin.readline().strip().split()
    print(S,G)
    # for i in range(len(Graph[S])):
    #     Queue.append(Graph[S][i])
    # print(Queue)
    minD = 50
    visited = [minD]*V
    BFS(S,0)
    if minD == 50:
        minD = 0
    print(minD)
'''


#성공
#함수부분
def BFS(d):
    global minD
    while Queue:
        s,d = Queue.pop(0)
        if s == G:
            minD = d
            break
        if visited[int(s)-1] == False:
            visited[int(s)-1] = True
            for i in Graph[s]:
                if visited[int(i)-1] == False:
                    Queue.append([i,d+1])
    return minD
# sys.stdin 사용
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Queue1/input_5102.txt", "r")
for tc in range(1, int(sys.stdin.readline())+1):
    V,E = map(int,sys.stdin.readline().strip().split())
    Graph = {str(i):[] for i in range(1,V+1)}
    for i in range(E):
        s,e = sys.stdin.readline().strip().split()
        Graph[s].append(e)
        Graph[e].append(s)
    S,G = sys.stdin.readline().strip().split()
    Queue = [[S,0]]
    visited = [False]*V
    minD = 50
    BFS(0)
    if minD == 50:
        minD = 0
    print('#%d'%tc,minD)

# input 사용
for tc in range(1, int(input())+1):
    V,E = map(int,input().split())
    Graph = {str(i):[] for i in range(1,V+1)}
    for i in range(E):
        s,e = input().split()
        Graph[s].append(e)
        Graph[e].append(s)
    S,G = input().split()
    Queue = [[S,0]]
    visited = [False]*V
    minD = 50
    BFS(0)
    if minD == 50:
        minD = 0
    print('#%d'%tc,minD)