'''
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9	 

출력
#1 1
#2 1
#3 1
'''

'''
# 0 using sys.stdin
import sys
def checkLine(s,g,Node):
    stack = []
    stack.append(s)
    print('initial stack is:',stack)
    connected = False
    while len(stack) != 0:
        v = stack[-1]
        print('current v is:',v)
        if len(Node[v]) != 0:
            if g in Node[v]:
                print(' lucky! found the connected line!')
                connected = True
                break                
            print(' v has some linked nodes:',Node[v])
            w = Node[v].pop()
            print(' v and changed Nove[v] and new w is:', v, Node[v], w)
            stack.append(w)
            print(' current stack is:',stack)
        else: 
            print(' but... does not have any linked nodes:',Node[v])
            stack.pop()
            print(' current stack is:',stack)
    return 1 if connected == True else 0
    
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Stack/input_4871.txt", "r")
T = sys.stdin.readline()
# print(type(T.strip()))
for tc in range(1, int(T)+1):
    V,E = map(int,sys.stdin.readline().strip().split())
    print('V is:',V,'and E is:',E)
    Nodes = {'{}'.format(i) : [] for i in range(1,V+1)}
    # print(Nodes)
    for j in range(E):
        start,end = map(str,sys.stdin.readline().strip().split())
        # print(start,end)
        Nodes[start].append(end)
    # print(Nodes[1])
    print(Nodes)
    S, G = map(str,sys.stdin.readline().split())
    print('S is :',S,'and G is: ',G)
    result = 0
    if int(S) in range(1,V+1) and int(G) in range(1,V+1):
        print('correct way')
        result = checkLine(S,G,Nodes)
    print(f'#{tc} {result}')
'''

# 1 using input()
def checkLine(s,g,Node):
    stack = []
    stack.append(s)
    connected = 0
    while len(stack) != 0:
        v = stack[-1]
        if len(Node[v]) != 0:
            if g in Node[v]:
                connected = 1
                break                
            w = Node[v].pop()
            stack.append(w)
        else: 
            stack.pop()
    return connected
T = int(input())
for tc in range(1, T+1):
    V,E = map(int,input().split())
    Nodes = {'{}'.format(i) : [] for i in range(1,V+1)}
    for j in range(E):
        start,end = map(str,input().split())
        Nodes[start].append(end)
    S, G = map(str,input().split())
    result = 0
    if int(S) in range(1,V+1) and int(G) in range(1,V+1):
        result = checkLine(S,G,Nodes)
    print(f'#{tc} {result}')