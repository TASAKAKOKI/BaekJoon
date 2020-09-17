# 0
import sys
sys.stdin = open("./SW_Expert_Academy강의/Programming Intermediate/파이썬SW문제해결기본_List1/input_4828.txt", "r")
T = sys.stdin.readlines()
for i in range(1,len(T)):
    if i%2==0:
        List = list(map(int,T[i].split()))
        print('#%d '%int(i/2) + str((max(List)-min(List))))

# 1
T =int(input())
for t in range(1,T+1):
    N = int(input())
    List = list(map(int,input().split()))
    print(f'#{t} {max(List)-min(List)}')