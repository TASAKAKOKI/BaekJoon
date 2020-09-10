# 방법 1 range활용하기
import sys
input = sys.stdin.readline;
T = int(input());
for i in range(T,0,-1):
    print(i);

# 방법 2 reversed 사용하기
import sys
input = sys.stdin.readline;
T = int(input());
a = list(reversed(range(1,T+1)));
for i in a:
    print(i);