# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5QSEhaA5sDFAUq&probBoxId=AV9gdM_anw0DFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part1&problemBoxCnt=20

'''
10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다)
'''

# sys.stdin 버전
import sys
sys.stdin = open("./SW_Expert_Academy/SW역량테스트준비/D1-D2문제풀이_기초다지기/홀수만 더하기.txt", "r")
for tc in range(1,int(sys.stdin.readline())+1):
    L = list(map(int,sys.stdin.readline().strip().split()))
    print('#%d'%tc,sum([i for i in L if i % 2 != 0]))

# input버전
for tc in range(1,int(input())+1):
    L = list(map(int,input().split()))
    print('#%d'%tc,sum([i for i in L if i % 2 != 0]))