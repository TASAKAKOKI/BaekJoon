# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
'''
N개의 10억 이하 자연수로 이뤄진 수열이 주어진다. 이 수열은 완성된 것이 아니라 M번의 편집을 거쳐 완성된다고 한다.
완성된 수열에서 인덱스 L의 데이터를 출력하는 프로그램을 작성하시오.

다음은 미완성 수열과 편집의 예이다.
    인덱스 0 1 2 3 4    
    수열   1 2 3 4 5
I 2 7 -> 2번 인덱스 앞에 7을 추가하고, 한 칸 씩 뒤로 이동한다.
    인덱스 0 1 2 3 4 5
    수열   1 2 7 3 4 5
D 4 -> 4번 인덱스 자리를 지우고, 한 칸 씩 앞으로 이동한다.
    인덱스 0 1 2 3 4
    수열   1 2 7 3 5
C 3 8 -> 3번 인덱스 자리를 8로 바꾼다.
    인덱스 0 1 2 3 4
    수열   1 2 7 8 5
만약 편집이 끝난 후 L이 존재하지 않으면 -1을 출력한다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L이 주어지고, 다음 줄에 수열이 주어진다.
그 다음 M개의 줄에 걸쳐 추가할 인덱스와 숫자 정보가 주어진다. 5<=N<=1000, 1<=M<=1000, 6<=L<=N+M

출력
#1 5
#2 10239
#3 -1
'''
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_LinkedList1/수열 편집.txt", "r")
def completeS():
    global S
    for _ in range(M):
        infos = input().split()
        info,idx = infos[0],int(infos[1])
        if info == 'D':
            S.pop(idx)
       	else:
            num = int(infos[2])
            if info == 'I':
        	    S[idx:0] = [num]
            else:
                S[idx] = num	        
    return S
# 0 using sys.stdin
for tc in range(1, int(sys.stdin.readline())+1):
    #N:수열의 길이, M:추가 횟수, L: 출력할 인덱스 번호
    N,M,L = map(int,sys.stdin.readline().strip().split())
    #S: 수열
    S = list(map(int,sys.stdin.readline().strip().split()))
    #M개의 줄에 걸쳐서 추가할 인덱스와 숫자 정보가 주어진다. 5<= N<=1000, 1<=M<= 1000, 6<L<=N+M
    completeS()
    # L이 인덳스의 범위 안에 있다면, result변수에 인덱스에해당하는 요소를, 없다면 -1을 저장
    if L in range(len(S)):
        result = S[L]
    else:
        result = -1
    # 각 테스트케이스 별로 완성 된 수열의 L인덱스의 요소를 출력
    print(f'#{tc} {result}')

'''
# 1 using input
def completeS():
    global S
    for _ in range(M):
        infos = input().split()
        info,idx = infos[0],int(infos[1])
        if info == 'D':
            S.pop(idx)
       	else:
            num = int(infos[2])
            if info == 'I':
        	    S[idx:0] = [num]
            else:
                S[idx] = num	        
    return S
for tc in range(1, int(input())+1):
    N,M,L = map(int,input().split())
    S = list(map(int,input().split()))
    completeS()
    result = -1
    if L in range(len(S)):
        result = S[L]
    print(f'#{tc} {result}')
    '''