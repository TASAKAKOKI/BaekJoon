# 0
import sys
sys.stdin = open("./SW_Expert_Academy/py-2/1926.txt", "r")
T = int(sys.stdin.readline())
print(T,type(T))
for i in range(1,T+1):
    j = str(i)
    count = 0
    if '3' in j or '6' in j or '9' in j:
        count += j.count('3')
        count += j.count('6')
        count += j.count('9')
        print(count*'-',end=' ')
    else:
        print(i,end=' ')    

# 1
T =int(input())
for i in range(1,T+1):
    j = str(i)
    count = 0
    if '3' in j or '6' in j or '9' in j:
        count += j.count('3')
        count += j.count('6')
        count += j.count('9')
        print(count*'-',end=' ')
    else:
        print(i,end=' ')      