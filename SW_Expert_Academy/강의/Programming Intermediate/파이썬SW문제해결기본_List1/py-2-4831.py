# 0
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_List1/input_4831.txt", "r")
T = sys.stdin.readlines()
for i in range(1,len(T),2):
    K,N,M = map(int,T[i].strip().split())
    S = [0]+list(map(int,T[i+1].strip().split()))+[N]
    result = 0
    posCur = 0
    while  S[posCur] < N:
        posCur = [j for j in range(len(S)) if j > posCur and S[j]-S[posCur] <= K]
        if posCur:
            posCur = max(posCur)
            result += 1;
        else:
            result = 1
            break;
    print(f'#{int((i+1)/2)} {result-1}')

# 1
T = int(input())
for i in range(1,T+1):
    K,N,M = map(int,input().split())
    S = [0]+list(map(int,input().split()))+[N]
    result = 0
    posCur = 0
    while  S[posCur] < N:
        posCur = [j for j in range(len(S)) if j > posCur and S[j]-S[posCur] <= K]
        if posCur:
            posCur = max(posCur)
            result += 1;
        else:
            result = 1
            break;
    print(f'#{i} {result-1}')