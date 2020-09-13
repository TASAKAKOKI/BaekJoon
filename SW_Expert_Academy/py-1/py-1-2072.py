# import sys
# sys.stdin = open("./SW_Expert_Academy/py-1/input.tex", "r")
# T = sys.stdin.readlines()
# for i in range(1,len(T)):
#     T[i] = list(map(int,T[i].strip().split()))
#     T[i] = list(filter(lambda x:x%2!=0, T[i]))
#     print(f'#{i} {sum(T[i])}')

T =int(input())
for t in range(1,T+1):
    List = list(map(int,input().split()))
    List = list(filter(lambda x:x%2!=0,List))
    print(f'#{t} {sum(List)}')