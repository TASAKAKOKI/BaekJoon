# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5P1kNKAl8DFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14

'''
패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.

[제약 사항]
각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

import sys
sys.stdin = open("./SW_Expert_Academy/SW역량테스트준비/D1-D2문제풀이_기초다지기/패턴 마디의 길이.txt", "r")

# 모범답안#####################################
#sys
for i in range(1,int(sys.stdin.readline())+1):
    Str = sys.stdin.readline().strip()
    for j in range(1,11):
        word = j
        if Str[:j] == Str[j:j+j]:
            break
    print(f"#{i} {word}")
#input
for i in range(1,int(input())+1):
    Str = input()
    for j in range(1,11):
        word = j
        if Str[:j] == Str[j:j+j]:
            break
    print(f"#{i} {word}")
###############################################

# sys.stdin 버전
for tc in range(1,int(sys.stdin.readline())+1):
    S = sys.stdin.readline().strip()
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
    S = input()
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