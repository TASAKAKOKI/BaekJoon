# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5LrsUaDxcDFAXc&probBoxId=AV9gdM_anw0DFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part1&problemBoxCnt=20

'''
연속된 N일 동안 물건의 매매가를 예지력으로 미리 알 수 있는 철수
당국의 감시를 피해 하루 1만큼만 구매 가능
판매에는 제한 없음
ex) A라는 물건이 첫째날 1, 둘째날 2, 셋째날 3에 거래된다면,
첫째날과 둘째날에 각각 1개씩 구매하여 3 지출
셋째날에 2개를 모두 6에 판매하여 3의 마진을 남긴다.

T는 총 테스트 케이스할 횟수
각 T에 대하여,
    N은 관찰할 N개의 날
    연속된 N개의 날에 대한 매매가가 주어진다. (각 날의 매매가는 최대 10,000)

이때, 주어진 조건에 대하여 최대 이익을 출력하는 프로그램 작성하기.
아무것도 사지 않는 것이 최대 이익인 경우 0을 출력
'''


# 1차 실패, 10개중 8개 성공
# 뒤에서 부터 계산해야 한다.
# why??
'''
# sys.stdin 버전
import sys
sys.stdin = open("./SW_Expert_Academy/SW역량테스트준비/D1-D2문제풀이_기초다지기/백만장자.txt", "r")
for tc in range(1,int(sys.stdin.readline())+1):
    N = int(sys.stdin.readline())
    L = list(map(int,sys.stdin.readline().strip().split()))
    S, margin = 0,0
    while S < N-1:
        newL = L[S:]
        if newL == sorted(newL,reverse=True):
            break
        eleList = [i for i in range(len(newL)) if newL[i] == max(newL)]
        idx = eleList[-1]
        for i in range(idx):
            margin += newL[idx] - newL[i]
        S += idx +1
    print('#%d'%tc,margin)

    
# input버전
for tc in range(1,int(input())+1):
    N = int(input())
    L = list(map(int,input().split()))
    S, margin = 0,0
    while S < N-1:
        newL = L[S:]
        if newL == sorted(newL,reverse=True):
            break
        eleList = [i for i in range(len(newL)) if newL[i] == max(newL)]
        idx = eleList[-1]
        for i in range(idx):
            margin += newL[idx] - newL[i]
        S += idx +1
    print('#%d'%tc,margin)
'''


# sys.stdin 버전
import sys
sys.stdin = open("./SW_Expert_Academy/SW역량테스트준비/D1-D2문제풀이_기초다지기/백만장자.txt", "r")
for tc in range(1,int(sys.stdin.readline())+1):
    N = int(sys.stdin.readline())
    L = list(map(int,sys.stdin.readline().strip().split()))
    margin,curMax = 0,0
    for i in range(N-1,-1,-1):
        if L[i] > curMax:
            curMax = L[i]
        else:
            margin += curMax - L[i]
    print('#%d'%tc,margin)

    
# input버전
for tc in range(1,int(input())+1):
    N = int(input())
    L = list(map(int,input().split()))
    margin,curMax = 0,0
    for i in range(N-1,-1,-1):
        if L[i] > curMax:
            curMax = L[i]
        else:
            margin += curMax - L[i]
    print('#%d'%tc,margin)
