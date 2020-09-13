T = int(input())
for t in range(1,T+1):
    array = list(map(int,input().split()))
    Sum = sum(array)
    Len = len(array)
    r = round(Sum/Len)
    print(f'#{t} {r}')