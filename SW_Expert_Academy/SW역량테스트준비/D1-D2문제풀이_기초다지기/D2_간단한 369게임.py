# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PTeo6AHUDFAUq&probBoxId=AV9gdM_anw0DFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part1&problemBoxCnt=20

'''
3 6 9 게임을 프로그램으로 제작중이다. 게임 규칙은 다음과 같다.
1. 숫자 1부터 순서대로 차례대로 말하되, “3” “6” “9” 가 들어가 있는 수는 말하지 않는다.
  1 2 3 4 5 6 7 8 9…
2. "3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.  
예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.
입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를
게임 규칙에 맞게 출력하는 프로그램을 작성하라.
박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.
여기서 주의해야 할 것은 박수 한 번 칠 때는 - 이며, 박수를 두 번 칠 때는 - - 가 아닌 -- 이다. 
 
[제약사항]
N은 10이상 1,000이하의 정수이다. (10 ≤ N ≤ 1,000)

[입력]
입력으로 정수 N 이 주어진다.

[출력]
1 ~ N까지의 숫자를 게임 규칙에 맞게 출력한다.
'''

# sys.stdin 버전
import sys
sys.stdin = open("./SW_Expert_Academy/SW역량테스트준비/D1-D2문제풀이_기초다지기/간단한 369게임.txt", "r")
L = [str(i) for i in range(1,int(sys.stdin.readline())+1)]
for n in L:
    count = 0
    count += n.count('3')
    count += n.count('6')
    count += n.count('9')
    if count != 0:
        n = '-'*count
    print(n,end=' ')

# input버전
L = [str(i) for i in range(1,int(input())+1)]
for n in L:
    count = 0
    count += n.count('3')
    count += n.count('6')
    count += n.count('9')
    if count != 0:
        n = '-'*count
    print(n,end=' ')