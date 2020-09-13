# 0
'''
import sys
sys.stdin = open("./SW_Expert_Academy/py-2/input.txt", "r")
T = sys.stdin.readlines()
for i in range(1,len(T)):
    T[i] = list(map(int,T[i].strip().split()))
    # P = T[i][0]
    # Q = T[i][1]
    # R = T[i][2]
    # S = T[i][3]
    # W = T[i][4]
    A = T[i][4]*T[i][0]
    B = 0
    Result = A
    if T[i][4] <= T[i][2]:
        B = T[i][1]
    else:
        B = T[i][1] + (T[i][4]-T[i][2])*T[i][3]
    if A > B:
        Result = B
    print(f'#{i} {Result}')
    # A = W*P
    # B = 0
    # Result = A
    # if W <= R:
    #     B = Q
    # else:
    #     B = Q + (W-R)*S
    # if A > B:
    #     Result = B
    # print(f'#{i} {Result}')

'''

# 1
T =int(input())
for t in range(1,T+1):
    List = list(map(int,input().split()))
    # P = List[0]
    # Q = List[1]
    # R = List[2]
    # S = List[3]
    # W = List[4]
    A = List[4]*List[0]
    B = 0
    Result = A
    if List[4] <= List[2]:
        B = List[1]
    else:
        B = List[1] + (List[4]-List[2])*List[3]
    if A > B:
        Result = B
    print(f'#{t} {Result}')

# 2
T =int(input())
for t in range(1,T+1):
    P, Q, R, S, W= (map(int,input().split()))
    A = W*P
    B = Q
    if W > R:
        B = Q + (W-R)*S
    if A > B:
        print(f'#{t} {B}')
    else:
        print(f'#{t} {A}')