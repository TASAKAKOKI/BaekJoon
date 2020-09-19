'''
어린이 알고리즘 교실의 선생님은 경우의 수 놀이를 위해, 그림처럼 가로x세로 길이가 10x20, 20x20인 직사각형 종이를 잔뜩 준비했다.
그리고 교실 바닥에 20xN 크기의 직사각형을 테이프로 표시하고, 이 안에 준비한 종이를 빈틈없이 붙이는 방법을 찾아보려고 한다. N이 30인 경우 다음 그림처럼 종이를 붙일 수 있다.
10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산하는 프로그램을 만드시오. 직사각형 종이가 모자라는 경우는 없다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 N이 주어진다. 10≤N≤300, N은 10의 배수

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
30
50
70	 

출력
#1 5
#2 21
#3 85
'''

# 0 using sys.stdin
import sys,math
# def facto(n):
#     return n * pacto(n-1) if n > 1 else 1
# print(facto(5))
# print(math.factorial(5))
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Stack/input_4869.txt", "r")
T = sys.stdin.readline()
# print(type(T.strip()))
for tc in range(1, int(T)+1):
    N = int(sys.stdin.readline().strip())
    # print(N,type(N))

    # space is representing total amount of boxes which taping area can contain when it is filled only by the 20*10 boxes.
    space = N // 10
    # total is representing total amount for taping area
    total = 1
    numberOf2colList = []
    # i is represent number of 20*20 boxes
    for i in range(1,(space//2)+1):
        temp = 1
        for j in range(i):
            temp *= space-i-j
        temp = temp // (math.factorial(i))
        square = 1<<i 
        numberOf2colList.append(temp*square)
    # print(numberOf2colList)
    for j in range(len(numberOf2colList)):
        total += numberOf2colList[j]
    print(f'#{tc} {total}')

# 1 using input()
import math
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    space = N // 10
        # space represents total amount of boxes that each taping area(with 20*N size) can contain when it only contains 20*10 boxes.
    result = 1
        # result represents total amount of taping areas.
    numberOf2colList = []
    for i in range(1,(space//2)+1):
        # i represents number of 20*20 boxes within taping area.
        temp = 1
        for j in range(i):
            temp *= space-i-j
            # temp represents new space while consider space to mean real-containg amount not just width.
        temp = temp // (math.factorial(i))
            # temp now represents (temp P i) (e.g 4P3 = 4 and 5P2 = 10) 
        square = 1<<i 
        numberOf2colList.append(temp*square)
    # print(numberOf2colList)
    for j in range(len(numberOf2colList)):
        result += numberOf2colList[j]
    print(f'#{tc} {result}')