import sys
oriN = sys.stdin.readline().strip();
N = oriN;
cycle = 0;
while(True):
    if int(N)<10:
        N = '0' + N[-1];
    R = N[1];
    N = str(int(N[0])+int(R));
    N = R + N[-1];
    cycle += 1;
    if(int(N) == int(oriN)):
        break;
print(cycle);

# whil(N != a):