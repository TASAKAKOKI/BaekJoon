'''
골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.
사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.
각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.
두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.
N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.
e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91
e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89

 e   1   2   3  도착
 1   0  18  34
 2  48   0  55
 3  18   7   0
출발
이 경우 최소 소비량은 89가 된다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10
 
출력
#1 89
#2 96
#3 139
'''
import  sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Advanced/응용_구현2_완전 검색/5189_전자키트.txt", "r")
# 이 문제는 우선 시작점(0)을 제외한 1부터 N-1번까지의 요소들을 순열로 만들 수 있는 순서들을 만든 뒤, 각 순열에 대해서 합을 구해보자.  
def DFS(s):
    global tempSum,minSum
    if tempSum > minSum:
        return
    else:
        visited[s] = True
        if False not in visited:            #모든 곳을 방문했다면,
            tempSum += Field[s][0]
            if tempSum < minSum:            #현재까지의 합이 minSum보다 작다면, minSum값 갱신.
                minSum = tempSum
            tempSum -= Field[s][0]
        else:                               #방문하지 않은 곳이 아직 있다면,
            for i in range(1,N):
                if not visited[i]:
                    tempSum += Field[s][i]
                    DFS(i)
                    tempSum -= Field[s][i]
        visited[s] = False

for tc in range(1,int(sys.stdin.readline())+1):
    N = int(sys.stdin.readline())
    Field = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
    tempSum = 0
    minSum = 100*N
    visited = [False]*N
    DFS(0)
    print('#%d'%tc,minSum)