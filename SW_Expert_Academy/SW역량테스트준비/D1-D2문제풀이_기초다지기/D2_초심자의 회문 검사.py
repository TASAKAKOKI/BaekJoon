# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PyTLqAf4DFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14

'''
"level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.

[제약 사항]
각 단어의 길이는 3 이상 10 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

입력
3
level     
samsung
eye        
 
출력
#1 1
#2 0
#3 1
'''
import sys
sys.stdin = open("./SW_Expert_Academy/SW역량테스트준비/D1-D2문제풀이_기초다지기/초심자의 회문 검사.txt", "r")
def check(word):
    Len =len(word)
    L = Len//2
    count=0
    for i in range(L):
        if word[i] == word[-i-1]:
            count+=1
            continue
        else:
            return 0
    return 1

# sys.stdin 버전
for tc in range(1,int(sys.stdin.readline())+1):
    word = list(sys.stdin.readline().strip())
    print('#%d'%tc,check(word))

# input버전
for tc in range(1,int(input())+1):
    word = input()
    print('#%d'%tc,check(word))