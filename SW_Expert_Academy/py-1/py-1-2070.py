T = int(input())
for t in range(1, T+1):
    A,B = map(int,input().split())
    R = '='
    if A>B:
        R = '>'
    elif A<B:
        R = '<' 
    print(f'#{t} {R}')