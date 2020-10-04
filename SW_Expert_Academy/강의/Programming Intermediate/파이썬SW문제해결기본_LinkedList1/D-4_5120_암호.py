# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
'''
##################
현재 풀이는 노가다 야매.
좀 더 좋은 풀이법 찾아볼것
#########################

################
모범답안
def crypto(pwd):
    pivot = 0
    start_num = pwd[pivot]

    for _ in range(1, K + 1):
        pivot += M

        if pivot > len(pwd):
            pivot -= len(pwd)

        if pivot == len(pwd):
            pwd.append(pwd[-1] + start_num)
        else:
            pwd.insert(pivot, pwd[pivot - 1] + pwd[pivot])

    return pwd


T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    password = list(map(int, input().split()))

    encrypted = list(reversed(crypto(password)))

    print(f'#{test_case}', end=' ')
    print(*encrypted[:10])
################

A사는 창립기념일 이벤트로 비밀번호 맞추기 대회를 열어, 최대 10개인 비밀번호를 맞추는 사람에게 기념품을 제공하기로 했다.
기념품을 받을 수 있도록 다음 조건에 맞는 비밀번호 찾기 프로그램을 작성하시오.
    - 1000이하의 숫자 N개가 주어진다. 이때 시작 숫자가 정해지고, 첫 번째 지정 위치가 된다.
    - 지정 위치부터 M번째 칸을 추가한다. 여기에 앞칸의 숫자와 뒤로 밀려난 칸의 숫자를 더해 넣는다. 추가된 칸이 새로운 지정 위치가 된다. 밀려난 칸이 없으면 시작 숫자와 더한다.
    - 이 작업을 K회 반복하는데, M칸 전에 마지막 숫자에 이르면 남은 칸수는 시작 숫자부터 이어간다.
    - 마지막 숫자부터 역순으로 숫자를 출력하면 비밀번호가 된다. 숫자가 10개 이상인 경우 10개까지만 출력한다.
다음은 N, M, K가 6, 3, 3이고, 주어진 숫자가 6, 2, 4, 9, 1, 5인 경우의 예이다. 6이 시작 숫자이자 첫번째 지정 위치가 된다.
6 2 4 9 1 5
(1) 3번째에 새로운 칸을 추가하고, 앞의 숫자 4와 뒤로 밀려난 9를 더해 칸을 채운다.
    6 2 4 - 9 1 5 
    6 2 4 13 9 1 5
(2) 다시 3칸 뒤에 새로운 칸을 추가하고, 앞 뒤 숫자를 더해 넣는다.
    6 2 4 13 9 1 - 5
    6 2 4 13 9 1 6 5
(3) 다시 3칸 뒤에 칸을 추가하고 앞 뒤 숫자를 더해 넣는다.
    6 - 2 4 13 9 1 6 5
결과:
6 8 2 4 13 9 1 6 5
암호는 역순인 5 6 1 9 13 4 2 8 6이 된다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 N, M, K가, 다음 줄에 1000이하의 자연수 N개가 주어진다. 3<=N, M, K<=1000

출력
#1 5 6 1 9 13 4 2 8 6
#2 1736 2514 778 169 667 498 329 715 386 958
#3 826 1494 668 954 375 1052 677 302 774 2234
'''
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_LinkedList1/암호.txt", "r")

# 0 using sys.stdin
for tc in range(1, int(sys.stdin.readline())+1):
    #N: 주어질 숫자의 개수, M: 새로 추가할 지정위치로부터 M번째 칸, K: 반복할 횟수
    N,M,K = map(int,sys.stdin.readline().strip().split())
    #L: 주어진 N개의 숫자 (3<=N<=1000, 3<=M, K<=1000)
    L,p = sys.stdin.readline().strip().split(), 0
    # MAKEIT()
    for i in range(K):
        p = (p+M)%len(L)
        curN = L[p]
        if p in range(1,len(L)):
            prevN = L[p-1]
            L[p:0] = [str(int(curN)+int(prevN))]
        else:
            p = len(L)
            prevN = L[-1]
            L.extend([str(int(curN)+int(prevN))])
    L.reverse()
    resultL = L[:10]
    result = ' '.join(resultL)
    print(f'#{tc} {result}')

    '''
    # 각 테스트케이스 별로 완성 된 수열의 맨 뒤 숫자부터 역순으로 10개를 출력한다.
    # 이를 위해, 새로운 리스트를 만들어, 그 안의 요소들을 각각 end=' '출력?
    print(f'#{tc}',end=' ')
'''

# 1 using input
'''
for tc in range(1, int(input())+1):
    N,M,K = map(int,input().split())
    result = mergeSeq()
    print(f'#{tc}',end=' ')
    for j in range(-1,-10,-1):
        print(result[j],end=' ')
    print(result[-10])
'''