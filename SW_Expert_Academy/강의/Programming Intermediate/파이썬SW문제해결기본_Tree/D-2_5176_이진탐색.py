'''
1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.
이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
추가나 삭제가 없는 경우에는, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들수 있다.
다음은 1부터 6까지의 숫자를 완전 이진 트리 형태인 이진 탐색 트리에 저장한 경우이다.
         1(4)
        /    \
     2(2)    3(6)
    /   \    /
 4(1)  5(3)6(5) 
완전 이진 트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다.
N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과, N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 N이 주어진다. 1<=N<=1000
 
출력
#1 4 6
#2 5 2
#3 8 14
'''
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Tree/이진탐색.txt", "r")
# 순서대로 1부터 N까지의 숫자를 인수로 받아, 해당 노드에 넣는 함수.
def makeTree(nodeNo):
    global number
    if nodeNo <= N:
        makeTree(nodeNo*2)
        Tree[nodeNo] = number
        number += 1
        makeTree(nodeNo*2+1)
# 0 using sys.stdin
for tc in range(1, int(sys.stdin.readline())+1):
    #N: 주어진 N의 값--> 1부터 N까지의 노드를 이진탐색트리가 되도록 삽입
    N = int(sys.stdin.readline())
    # 우선 Tree를 첫번째 값(인덱스 0)을 비워두고, 총 N개의 0값을 갖는 리스트를 만든다. 즉, 총 길이는 N+1이 된다.
    Tree = [0 for i in range(N+1)]
    # number는 노드의 번호를 의미할 것. 이진탐색트리의 경우, 각 노드가 2개까지의 노드를 자식으로 가지므로, 항상 왼쪽 자식노드는 2의 배수이고, 오른쪽 자식노드는 홀수이며, 가장 왼편에 위치하게 되는 노드들은 각각 2의 제곱의 노드 번호를 갖게된다. 
    number = 1
    makeTree(number)
    print('#%d'%tc,Tree[1],Tree[N//2])

# 1 using input
for tc in range(1, int(input())+1):
    N = int(input())
    Tree = [0 for i in range(N+1)]
    number = 1
    makeTree(number)
    print('#%d'%tc,Tree[1],Tree[N//2])