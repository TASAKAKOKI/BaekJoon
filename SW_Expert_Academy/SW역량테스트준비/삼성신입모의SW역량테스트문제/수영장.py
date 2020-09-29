# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PpFQaAQMDFAUq&probBoxId=AV732SG66sEDFAW7&type=PROBLEM&problemBoxTitle=%EC%82%BC%EC%84%B1+%EC%8B%A0%EC%9E%85+%EB%AA%A8%EC%9D%98+sw+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AC%B8%EC%A0%9C%EB%AA%A8%EC%9D%8C&problemBoxCnt=10

import sys
sys.stdin = open("./SW_Expert_Academy/SW역량테스트준비/삼성신입모의SW역량테스트문제/input_수영장.txt", "r")

# def DFS(i,Sum):
#     global minSum
#     print(i)
#     print(Sum,minSum)
#     # print(type(Sum),type(minSum))
#     if Sum >= minSum:
#         return
#     if i == 11:
#         if Sum < minSum:
#             minSum = Sum
#     else:
#         if i < 10:
#             for j in range(2):
#                 if j == 0:
#                     temp = compDM(i)
#                     DFS(i+1,Sum+temp)
#                 else:
#                     if i != 9:
#                         DFS(i+3,Sum+threeM)

#         else:
#             temp = compDM(i)
#             DFS(i+1,Sum+temp)
#     return minSum

# def DFS(i,Sum):
#     global minSum
#     # if Sum >= minSum:
#     #     return
#     if i > 11:
#         if Sum < minSum:
#             minSum = Sum
#             print(visited)
#             return minSum
#     else:
#         if i < 10 and Plan[i] == 0 and Plan[i+1] == 0 and Plan[1+2] == 0:
#             DFS(i+1,Sum)
#         else:
#             if i < 10:
#                 for j in range(2):
#                     if j == 0:
#                         temp = compDM(i)
#                         visited[i] = 1
#                         DFS(i+1,Sum+temp)
#                         visited[i] = 0
#                     else:
#                         visited[i] = 3
#                         if i != 9:
#                             DFS(i+3,Sum+threeM)
#                         visited[i] = 0

#             else:
#                 temp = compDM(i)
#                 visited[i] = 1
#                 DFS(i+1,Sum+temp)
#                 visited[i] = 0

def compDM(i):
    if Plan[i] != 0:
        if Plan[i] * oneD > oneM:
            return oneM
        return Plan[i] * oneD
    return 0

def DFS(Sum):
    global minSum
    print(visited)
    for i in range(12):
        if visited[i] != 0:
            continue
        else:
            if i < 10:
                if Plan[i]==0 and Plan[i+1]==0 and Plan[i+1]==0:
                    visited[i] = 1
                    DFS(Sum)
                else:
                    if:
                        visited[i] = 1
                        DFS(Sum + DorM[i])
                    else:
                        Sum+threeM)
            else:
                visited[i],visited[i+1],visited[i+2] = 1,1,1
                DFS(Sum+DorM[i])
        else: continue

for case in range(int(sys.stdin.readline())):
    oneD,oneM,threeM,oneY = map(int,sys.stdin.readline().strip().split())
    print(oneD,oneM,threeM,oneY)
    Plan = list(map(int,sys.stdin.readline().strip().split()))
    print(Plan)
    DorM = [compDM(i) for i in range(12)]
    print(DorM)
    minSum = oneY
    visited = [0] * 12
    DFS(0)
    # print('#%d'% (case+1),minSum)


'''
def compDM(i):
    if Plan[i] != 0:
        if Plan[i]*oneD > oneM:
            return oneM
        return Plan[i]*oneD
    return 0

def DFS(i,Sum):
    global minSum
    if Sum >= minSum:
        return
    if i > 11:
        if Sum < minSum:
            minSum = Sum
            print(visited)
    else:
        if i < 10:
            for j in range(2):
                if j == 0:
                    temp = compDM(i)
                    visited[i] = 1
                    DFS(i+1,Sum+temp)
                    visited[i] = 0
                else:
                    visited[i] = 3
                    if i != 9:
                        DFS(i+3,Sum+threeM)
                    visited[i] = 0

        else:
            temp = compDM(i)
            visited[i] = 1
            DFS(i+1,Sum+temp)
            visited[i] = 0
    return minSum
            
for case in range(int(input())):
    oneD,oneM,threeM,oneY = map(int,input().split())
    Plan = list(map(int,input().split()))
    DorM = [compDM(i) for i in range(12)]
    minSum = oneY
    visited=[0]*12
    DFS(0,0)
    print('#%d'% (case+1),minSum)
'''
