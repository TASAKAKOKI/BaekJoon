# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

'''
트리의 일부를 서브 트리라고 한다. 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.
주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체의 루트 노드가 된다.
이런 경우의 트리는 부모 노드를 인덱스로 다음과 같은 방법으로 나타낼 수 있다. 자식 노드가 0인 경우는 노드가 자식이 없는 경우이다.
    2
   1 5
  6   3
 4
부모   1 2 3 4 5 6
자식1  6 1 0 0 3 4
자식2  0 5 0 0 0 0

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 간선의 개수 E와 N이 주어지고, 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.
노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1
 
출력
#1 3
#2 1
#3 3
'''
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Tree/subtree.txt", "r")
def countNodes(curNode):
    global count
    if Tree[curNode]:
        count += len(Tree[curNode])
        for node in Tree[curNode]:
            countNodes(node)
    else:
        return count

# 0 using sys.stdin
for tc in range(1, int(sys.stdin.readline())+1):
    #E: 주어질 간선의 개수 , N: 루트로 지정할 노드
    E,N = map(int,sys.stdin.readline().strip().split())
    #E개의 부모 자식 노드 번호 쌍이 한줄로 주어진다. 
    #노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1

    # N에대하여, 1번부터 N+1번까지의 노드를 갖는 트리를 생성. 이때, 각 노드의 값은 자식노드를 담은 리스트이지만, 초기화시에는 빈 리스트를 값으로 준다.
    Tree = {str(i):[] for i in range(1,E+2)}
    # Edge에 주어진 간선정보들을 담는다.
    Edges = sys.stdin.readline().strip().split()
    # 주어진 간선정보를 토대로, 부모노드를 키로, 자식노드들의 집합리스트를 값으로 갖는 딕셔너리 Tree 생성
    for i in range(len(Edges)):
        if i%2==0:
            Pnode = Edges[i]
        else:
            Cnode = Edges[i]
            Tree[Pnode].append(Cnode)
    count = 1
    # 주어진 노드의 자식 노드를 카운팅 하는 함수 호출
    countNodes(str(N))
    # 각 테스트케이스 별로 완성 된 수열의 L인덱스의 요소를 출력
    print('#%d'%tc,count)

# 1 using input
T = int(input())
for tc in range(1, T+1):
    E,N = map(int,input().split())
    Tree = {str(i):[] for i in range(1,E+2)}
    Edges = input().split()
    for i in range(len(Edges)):
        if i%2==0:
            Pnode = Edges[i]
        else:
            Cnode = Edges[i]
            Tree[Pnode].append(Cnode)
    count = 1
    countNodes(str(N))
    print('#%d'%tc,count)