'''
작업 시작 시간(s)와 작업 종료 시간(e)를 원소로 삼는 튜플로 리스트를 구성한다.
리스트를 우선 튜플 값을 기준으로 정렬한다.
start를 0으로 초기화한다.
for 리스트내의 원소 들중 s값이 start보다 큰 원소들에 대해서:
    early 종료시간을 24로 초기화한다.
    리스트를 순회하며, 가장 작은 early 값을 갖는 튜플을 찾고, 그 값을 start 변수에 저장한다.
'''
import  sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Advanced/응용_구현3_탐욕 알고리즘/5202_화물 도크.txt", "r")
for T in range(1,int(sys.stdin.readline())+1):
    N = int(sys.stdin.readline())
    taskList = [tuple(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
    taskList.sort(key=lambda task: task[1])
    S, tCount = 0,0
    while True:
        remain = [t for t in taskList if t[0] >= S]
        if remain:
            S = remain[0][1]
            tCount += 1
            continue
        else:
            break
    print('#%d'%T,tCount)

for T in range(1,int(input())+1):
    N = int(input())
    taskList = [tuple(map(int,input().split())) for _ in range(N)]
    taskList.sort(key=lambda task: task[1])
    S, tCount = 0,0
    while True:
        remain = [t for t in taskList if t[0] >= S]
        if remain:
            S = remain[0][1]
            tCount += 1
            continue
        else:
            break
    print('#%d'%T,tCount)