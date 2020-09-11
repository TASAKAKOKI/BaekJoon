import sys
i = sys.stdin.readline;
T = int(i());
for n in range(1,T+1):
    a,b = map(int,i().split());
    print(f'Case #{n}: {a+b}');