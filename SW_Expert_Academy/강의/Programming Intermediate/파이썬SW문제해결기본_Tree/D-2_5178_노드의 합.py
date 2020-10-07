'''
클래스 사용한 모범답안
'''

'''
완전 이진 트리의 리프 노드에 1000이하의 자연수가 저장되어 있고, 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다고 한다.
다음은 리프 노드에 저장된 1, 2, 3이 주어졌을 때, 나머지 노드에 자식 노드의 합을 저장한 예이다.
         1( )                      1(6)
        /    \                    /   \
    2( )     3(3)              2(3)    3(3)
    /  \                      /   \     
 4(1) 5(2)                  4(1)  5(2) 
 리프 노드 저장 값          자식 노드의 합을 저장한 상태
N개의 노드를 갖는 완전 이진 트리의 노드 번호는 루트가 1번이 되며, 같은 단계에서는 왼쪽에서 오른쪽으로 증가, 단계가 꽉 차면 다음단계의 왼쪽부터 시작된다.
완전 이진 트리의 특성상 1번부터 N번까지 빠지는 노드 번호는 없다.
리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음, 지정한 노드 번호에 저장된 값을 출력하는 프로그램을 작성 하시오.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L이 주어지고, 다음 줄부터 M개의 줄에 걸쳐 리프 노드 번호와 1000이하의 자연수가 주어진다.

출력
#1 3
#2 845
#3 1801
'''
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Tree/노드의 합.txt", "r")
# sys.stdin사용
class Tree:
    def __init__(self,n):
        self.TList = [0]*(n+1)
    def addAtLeafNode(self,node,number):
        self.TList[node] = number
    def makeNodeSum(self):
        Len = len(self.TList) - M
        for i in range(Len-1,0,-1):
            if self.TList[i]:
                print('i is:',i)
                continue
            else:
                if i*2+1 in range(len(self.TList)):
                    self.TList[i] = self.TList[i*2] + self.TList[i*2+1]
                else:
                    self.TList[i] = self.TList[i*2]
for tc in range(1, int(sys.stdin.readline())+1):
    # N: 노드의 개수, M: 리프 노드의 개수, L: 값을 출력할 노드 번호
    N,M,L = map(int,sys.stdin.readline().strip().split())
    # T: 클라스 Tree를 생성
    T = Tree(N)
    for i in range(M):
        L_Node,n = map(int,sys.stdin.readline().strip().split())
        T.addAtLeafNode(L_Node,n)
    T.makeNodeSum()
    print('#%d'%tc,T.TList[L])
'''
    for i in list(map(int,sys.stdin.readline().strip().split())):
        T.add(i)
    print('#%d'%tc,T.totalSum())
'''