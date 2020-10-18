'''
    ㄱ. 우선 트럭의 적재용량과 화물의 무게 리스트를 내림차순으로 정렬한다.
    변수 화물의 무게를 0으로 초기화
    ㄴ. 적재용량이 가장 큰 트럭과 가장 무거운 화물을 비교한다.
      for 화물의 무게 리스트의 크기만큼 반복
        if 두 리스트가 비어있지 않다면:
            if 적재용량 >= 화물의 무게:
                화물의 무게 리스트와 적재용량 리스트에서 각각의 최대값을 제거한다.
                변수 화물의 무게에 현재 최대 값인 마지막 화물의 무게를 더한다.
            else (적재용량 < 화물의 무게):
                화물의 무게 리스트에서 최대값을 제거한다.
        else (하나라도 빈 리스트라면):
            break
    화물의 무게를 결과값으로 도출한다.
'''
import  sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Advanced/응용_구현3_탐욕 알고리즘/5201_컨테이너 운반.txt", "r")
for tc in range(1,int(sys.stdin.readline())+1):
    N,M = map(int,sys.stdin.readline().strip().split())
    Weights = list(map(int,sys.stdin.readline().strip().split()))
    Capacities = list(map(int,sys.stdin.readline().strip().split()))
    maxWeight = 0
    Weights.sort(), Capacities.sort()
    for i in range(len(Weights)):
        if Capacities and Weights:
            if Weights[-1] <= Capacities[-1]:
                maxWeight += Weights.pop()
                Capacities.pop()
            else:
                Weights.pop()
        else:
            break
    print('#%d'%tc, maxWeight)

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    Weights = list(map(int,input().split()))
    Capacities = list(map(int,input().split()))
    maxWeight = 0
    Weights.sort(), Capacities.sort()
    for i in range(len(Weights)):
        if Capacities and Weights:
            if Weights[-1] <= Capacities[-1]:
                maxWeight += Weights.pop()
                Capacities.pop()
            else:
                Weights.pop()
        else:
            break
    print('#%d'%tc, maxWeight)