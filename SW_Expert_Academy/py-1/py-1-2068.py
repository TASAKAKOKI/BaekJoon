T = int(input())
for t in range(1,T+1):
    array = list(map(int,input().split()))
    print(f'#{t} {sorted(array)[-1]}')