# sys.stdin.readline 사용한 경우
import sys
input = sys.stdin.readline;
T = int(input());
for i in range(T):
    a, b = map(int, input().split());
    print(a+b);

## input사용할 경우
T = int(input());
for i in range(T):
    a, b = map(int, input().split());
    print(a+b);
## 결과 : 시간초과 