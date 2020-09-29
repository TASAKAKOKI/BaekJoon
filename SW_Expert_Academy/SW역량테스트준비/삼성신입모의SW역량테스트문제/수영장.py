# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PpFQaAQMDFAUq&probBoxId=AV732SG66sEDFAW7&type=PROBLEM&problemBoxTitle=%EC%82%BC%EC%84%B1+%EC%8B%A0%EC%9E%85+%EB%AA%A8%EC%9D%98+sw+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AC%B8%EC%A0%9C%EB%AA%A8%EC%9D%8C&problemBoxCnt=10

##우선 테스트는 통과했지만, 코드는 다시 짜봐야 한다.
# DFS를 재귀로 다시 이용해보자.


import sys
sys.stdin = open("./SW_Expert_Academy/SW역량테스트준비/삼성신입모의SW역량테스트문제/input_수영장.txt", "r")

def DFS():
    global minSum, Stack
    while Stack:
        i,j,Sum = Stack.pop()
        if Sum > minSum:
            continue
        if i == 11 or (i == 9 and j == 3): #12월 이거나, 10월인데 3개월치를 끊은 경우, 마지막 계산이므로, 현재의 Sum과 현재 minSum값을 비교하여 결과를 낸다.
            if Sum < minSum:
                minSum = Sum
            continue
        if j == 1: # i월에 1일권 혹은 1개월치 중 싼 것을 끊은 경우
            if i <= 8: # 1월 ~ 9월까지는 다음 달에 3개월치를 끊거나, 1개월치(1일권)를 끊는 경우의 수를 부여해 줄 수 있다.  
                i += 1
                Stack.append([i,3,Sum+threeM])
                Stack.append([i,1,Sum+DorM[i]])
                continue
            else : # 10월 또는 11월의 경우, 다음 달에 1개월치를 끊는 경우만 부여해 줄 수 있다.
                i += 1
                Stack.append([i,1,Sum+DorM[i]])
                continue
        else: # (j==3) 즉 i월에 3개월치를 끊은 경우
            if i < 7: # 1월~6월까지는 다음 3개월 뒤에 1개월(1일)권 혹은 3개월권 두가지 경우의 수를 모두 고려할 수 있다.
                i += 3
                Stack.append([i,3,Sum+threeM])
                Stack.append([i,1,Sum+DorM[i]])
                continue
            else: # i == 7 or i == 8(즉, 8월 9월에 세달권을 끊은 경우, 다음 달이 11월,12월이 되므로 할 수 있는 선택지는, 그 달에 1달 이용권을 끊게 하는 경우 뿐이다.)
                i += 3
                Stack.append([i,1,Sum+DorM[i]])
                continue
    return minSum

for case in range(int(sys.stdin.readline())):
    oneD,oneM,threeM,oneY = map(int,sys.stdin.readline().strip().split())
    print(oneD,oneM,threeM,oneY)
    Plan = list(map(int,sys.stdin.readline().strip().split()))
    print(Plan)
    DorM = [oneM if Plan[i]*oneD > oneM else Plan[i]*oneD for i in range(12)]
    print(DorM)
    minSum = oneY
    Stack = [[0,3,threeM],[0,1,DorM[0]]]
    DFS()
    print('#%d'% (case+1),minSum)


# input()
def DFS():
    global minSum, Stack
    while Stack:
        # print(Stack)
        i,j,Sum = Stack.pop()
        if Sum > minSum:
            continue
        if i == 11 or (i == 9 and j == 3):
            if Sum < minSum:
                minSum = Sum
            continue
        if j == 1:
            if i <= 8:
                i += 1
                Stack.append([i,3,Sum+threeM])
                Stack.append([i,1,Sum+DorM[i]])
                continue
            else :
                i += 1
                Stack.append([i,1,Sum+DorM[i]])
                continue
        else:
            if i < 7:
                i += 3
                Stack.append([i,3,Sum+threeM])
                Stack.append([i,1,Sum+DorM[i]])
                continue
            else:
                i += 3
                Stack.append([i,1,Sum+DorM[i]])
                continue
    return minSum
for case in range(int(input())):
    oneD,oneM,threeM,oneY = map(int,input().split())
    # print(oneD,oneM,threeM,oneY)
    Plan = list(map(int,input().split()))
    # print(Plan)
    DorM = [oneM if Plan[i]*oneD > oneM else oneD*Plan[i] for i in range(12)]
    # print(DorM)
    minSum = oneY
    Stack = [[0,3,threeM],[0,1,DorM[0]]]
    DFS()
    print('#%d'% (case+1),minSum)