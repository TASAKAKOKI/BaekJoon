# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5P1kNKAl8DFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14

'''
크기가 N인 파스칼의 삼각형을 만들어야 한다.
파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
N이 4일 경우,
        1
      1   1
    1   2   1
  1   3   3   1
N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.

[제약 사항]
파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.

[출력]
각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.
삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

import sys
sys.stdin = open("./SW_Expert_Academy/SW역량테스트준비/D1-D2문제풀이_기초다지기/파스칼의 삼각형.txt", "r")

# 모범답안#####################################
#sys
# for i in range(1,int(sys.stdin.readline())+1):

#input
# for i in range(1,int(input())+1):

###############################################

# sys.stdin 버전
for tc in range(1,int(sys.stdin.readline())+1):
    N = int(sys.stdin.readline())
    # N은 1이상 10이하
    for i in range(N):
        i가 1일때,
            1 
        i가 2일때,
            1 1
        i가 3일때,
            1 (1+1) 1
            1   2   1
        i가 4일때,
            1 (1+(1+1)) ((1+1)+1) 1
            1     3         3     1
        i가 5일때,
            1 (1+(1+(1+1))) ((1+(1+1))+((1+1)+1)) (((1+1)+1)+1) 1 
            1       4                 6                 4       1
        print()
    
    n,s = 1, S[0]
    for i in range(1,len(S)):
        if S[i] != s:
            n += 1
        else:
            m = 1
            for j in range(1,n):
                if S[i+j] == S[j]:
                    m += 1
                else: break
            if n == m:
                break
            else:
                n += 1
                continue
    print('#%d'%tc,n)


# input버전
for tc in range(1,int(input())+1):
    N = int(input())

    n,s = 1, S[0]
    for i in range(1,len(S)):
        if S[i] != s:
            n += 1
        else:
            m = 1
            for j in range(1,n):
                if S[i+j] == S[j]:
                    m += 1
                else: break
            if n == m:
                break
            else:
                n += 1
                continue
    print('#%d'%tc,n)