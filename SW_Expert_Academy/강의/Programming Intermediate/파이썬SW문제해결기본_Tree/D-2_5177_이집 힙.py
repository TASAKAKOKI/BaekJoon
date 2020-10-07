'''
클래스 사용한 모범답안
class Tree:
    def __init__(self):
        self.lst = [0]

    def sort(self, num):
        if num >= 2:
            if self.lst[num] < self.lst[num//2]:
                #자리 바꾸기
                self.lst[num], self.lst[num//2] = self.lst[num//2], self.lst[num]
                self.sort(num//2) # 계속 정렬

    def append(self, data):
        num = len(self.lst)
        self.lst.append(data)
        self.sort(num)

    def my_sum(self, node):
        if node <= 1:
            return self.lst[node]
        else:
            return self.lst[node] + self.my_sum(node//2)

    def my_result(self):
        last = len(self.lst) - 1
        self.sum = 0
        if last >= 2:
            return self.my_sum(last//2)
        else:
            return 0
        

T = int(input())
for test_case in range(1, 1 + T):
    N = int(input()) # 안씀
    tree = Tree()
    for i in map(int, input().split()):
        tree.append(i)
    print('#{} {}'.format(test_case, tree.my_result()))
'''

'''
이진 최소힙은 다음과 같은 특징을 가진다.
    - 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
    - 부모 노드의 값<자식 노드의 값을 유지한다. 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.
    - 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더 이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.
예를 들어 7, 2, 5, 3, 4, 6이 차례로 입력되면 다음과 같은 트리가 구성된다.
         1(2)
        /    \
    2(3)     3(5)
    /  \     /
 4(7) 5(4) 6(6)
이때 마지막 노드인 6번의 조상은 3번과 1번 노드이다.
1000000이하인 N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고, 마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램을 작성하시오.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 N이 주어지고, 다음 줄에 1000000이하인 서로 다른 N개의 자연수가 주어진다. 5<=N<=500 

출력
#1 7
#2 5
#3 65
'''
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Tree/이진 힙.txt", "r")
'''
def makeBMinHeap(node):
    if node < N:
        temp = data[node]
        for i in range(1,N+1):
            # 루트노드값보다 새로운 삽입값이 큰 경우,
            if not Tree[i]:
                Tree[i] = data[node]
            elif Tree[i] < temp:
                if not Tree[i*2]:
                    Tree[i*2] = temp
                elif not Tree[i*2+1]:
                    Tree[i*2+1] = temp
                else:
                    continue
                makeBMinHeap(node+1)
                break
            # 루트노드값보다 새로운 삽입값이 작은 경우,
            else:
                temp = Tree[i]
                Tree[i] = data[node]
                if not Tree[i*2]:
                    Tree[i*2] = temp
                elif not Tree[i*2+1]:
                    Tree[i*2+1] = temp
                else:
                    continue
                makeBMinHeap(node+1)
                break
def calculSum(n,Sum):
    while n != 0:
        n //= 2
        Sum += Tree[n]
    return Sum
# 0 실패__ using sys.stdin 
for tc in range(1, int(sys.stdin.readline())+1):
    # N: 주어질 간선의 개수 , N: 루트로 지정할 노드
    N = int(sys.stdin.readline())
    # 1,000,000 이하의 서로 다른 N개의 자연수가 주어지므로, 이를 data리스트에 담는다.
    data = list(map(int,sys.stdin.readline().strip().split()))
    Tree = [0 for i in range(N+1)]
    # Tree[1] = data[0]
    makeBMinHeap(0)
    result = calculSum(N,0)
    print('#%d'%tc,result)
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
'''

# 2차도전, sys.stdin사용
    class Tree:
        def __init__(self):
            self.TList = [0]
        def sort(self,n):
            if n >= 2:
                if self.TList[n] < self.TList[n//2]:
                    self.TList[n],self.TList[n//2] = self.TList[n//2],self.TList[n]
                    self.sort(n//2)
        def add(self,node):
            n = len(self.TList)
            self.TList.append(node)
            self.sort(n)
        def Sum(self,curSum):
            n = len(self.TList)
            while n > 1:
                n //= 2
                curSum += self.TList[n]
            return curSum
    for tc in range(1, int(sys.stdin.readline())+1):
        # N: 루트로 지정할 노드의 개수
        N = int(sys.stdin.readline())
        # T: 클라스 Tree를 생성
        T = Tree()
        for i in list(map(int,sys.stdin.readline().strip().split())):
            T.add(i)
        print('#%d'%tc,T.Sum(0))

