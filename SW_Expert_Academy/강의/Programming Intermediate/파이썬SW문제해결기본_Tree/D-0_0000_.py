# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
'''
N개의 10억 이하 자연수로 이뤄진 수열이 주어진다.
이 수열은 완성된 것이 아니라 M개의 숫자를 지정된 위치에 추가하면 완성된다고 한다.
완성된 수열에서 인덱스 L의 데이터를 출력하는 프로그램을 작성하시오.
다음은 숫자를 추가하는 예이다.
인덱스 0 1 2 3 4
수열   1 2 3 4 5
2 7 -> 2번 인덱스에 7을 추가하고 한 칸 씩 뒤로 이동한다.
인덱스 0 1 2 3 4 5
수열   1 2 7 3 4 5
4 8 -> 4번 인덱스에 8을 추가하고 한 칸 씩 뒤로 이동한다.
인덱스 0 1 2 3 4 5 6
수열   1 2 7 3 8 4 5

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L이 주어지고, 다음 줄에 수열이 주어진다.
그 다음 M개의 줄에 걸쳐 추가할 인덱스와 숫자 정보가 주어진다. 5<=N<=1000, 1<=M<=1000, 6<=L<=N+M

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
  
출력
#1 4
#2 32402
#3 13398
'''
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_LinkedList1/숫자 추가.txt", "r")
def addInS(idx,num):
    global S
    S = S[:idx] + [num] + S[idx:]

# 0 using sys.stdin
for tc in range(1, int(sys.stdin.readline())+1):
    #N:수열의 길이, M:추가 횟수, L: 출력할 인덱스 번호
    N,M,L = map(int,sys.stdin.readline().strip().split())
    #S: 수열 수열을 linked list로 구현해야 하므로, class 생성해야 할까? 우선은 자리이동으로 인한 실행횟수는 많겠지만, 간단하게 리스트만으로 구현해보자.
    S = list(map(int,sys.stdin.readline().strip().split()))
    #M개의 줄에 걸쳐서 추가할 인덱스와 숫자 정보가 주어진다. 5<= N<=1000, 1<=M<= 1000, 6<L<=N+M
    for i in range(M):
        idx,num = map(int,sys.stdin.readline().strip().split())
        addInS(idx,num)
    # 각 테스트케이스 별로 완성 된 수열의 L인덱스의 요소를 출력
    print(f'#{tc} {S[L]}')

# 1 using input
T = int(input())
for tc in range(1, T+1):
    N,M,L = map(int,input().split())
    S = list(map(int,input().split()))
    for i in range(M):
        idx,num = map(int,input().split())
        addInS(idx,num)
    print(f'#{tc} {S[L]}')