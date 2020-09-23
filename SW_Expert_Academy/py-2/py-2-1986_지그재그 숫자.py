# 0
import sys
sys.stdin = open("./SW_Expert_Academy/py-2/1986.txt", "r")
T = int(sys.stdin.readline())
for tc in range(1,T+1):
    N = int(input())
    result = 0
    for i in range(1,N+1):
        if i % 2 == 0:
            result -= i
        else: 
            result += i
    print('#%d'%tc,result)

# 1
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = 0
    for i in range(1,N+1):
        if i % 2 == 0:
            result -= i
        else: 
            result += i
    print('#%d'%tc,result)