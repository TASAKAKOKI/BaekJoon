# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
'''
여러 개의 수열을 정해진 규칙에 따라 합치려고 한다. 다음은 3개의 수열이 주어진 경우의 예이다.
수열 1
2 3 4 5 
수열 2
4 8 7 6
수열 3
9 10 15 16
수열 4
1 2 6 5
수열 2의 첫 숫자 보다 큰 수자를 수열 1에서 찾아 그 앞에 수열 2를 끼워 넣는다.
2 3 4 4 8 7 6 5
합쳐진 수열에 대해, 수열 3의 첫 숫자보다 큰 숫자를 찾아 그 앞에 수열 3을 끼워 넣는다. 큰 숫자가 없는 경우 맨 뒤에 붙인다.
2 3 4 4 8 7 6 5 9 10 15 16
마지막 수열까지 합치고 나면, 맨 뒤의 숫자부터 역순으로 10개를 출력한다.
1 2 6 5 2 3 4 4 8 7 6 5 9 10 15 16

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 수열의 개수 M, 이후 M개의 줄에 걸쳐 1000이하의 자연수로 구성된 수열이 주어진다. 4<=N<=1000, 1<=M<=1000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 완성된 수열의 맨 뒤부터 10개의 숫자를 역순으로 출력한다.

출력
#1 16 15 10 9 5 6 7 8 4 4
#2 251 798 365 506 494 193 675 387 334 224
#3 404 483 16 788 123 274 231 659 778 178
'''
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_LinkedList1/수열 합치기.txt", "r")

# 0 using sys.stdin
def mergeSeq():
    curSeq = list(map(int,sys.stdin.readline().strip().split()))
    for i in range(M-1):
        newSeq = list(map(int,sys.stdin.readline().strip().split()))
        lenCurSeq = len(curSeq)
        for i in range(len(curSeq)):
            if curSeq[i] > newSeq[0]:
                curSeq[i:0] = newSeq
                break
        if len(curSeq) == lenCurSeq:
            curSeq += newSeq
    return curSeq
for tc in range(1, int(sys.stdin.readline())+1):
    #N:수열의 길이, M:수열의 개수
    N,M = map(int,sys.stdin.readline().strip().split())
    #M개의 줄에 걸쳐서 1000이하의 자연수로 구성된 수열이 주어진다. 4<= N<=1000, 1<=M<= 1000
    result = mergeSeq()
    # 각 테스트케이스 별로 완성 된 수열의 맨 뒤 숫자부터 역순으로 10개를 출력한다.
    # 이를 위해, 새로운 리스트를 만들어, 그 안의 요소들을 각각 end=' '출력?
    print(f'#{tc}',end=' ')
    for j in range(-1,-10,-1):
        print(result[j],end=' ')
    print(result[-10])

# 1 using input
def mergeSeq():
    curSeq = list(map(int,input().split()))
    for i in range(M-1):
        newSeq = list(map(int,input().split()))
        lenCurSeq = len(curSeq)
        for i in range(len(curSeq)):
            if curSeq[i] > newSeq[0]:
                curSeq[i:0] = newSeq
                break
        if len(curSeq) == lenCurSeq:
            curSeq += newSeq
    return curSeq
for tc in range(1, int(input())+1):
    N,M = map(int,input().split())
    result = mergeSeq()
    print(f'#{tc}',end=' ')
    for j in range(-1,-10,-1):
        print(result[j],end=' ')
    print(result[-10])