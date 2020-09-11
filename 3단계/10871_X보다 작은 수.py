import sys
i=sys.stdin.readline
N,X=map(int,i().split())
A=list(filter(lambda a: a< X,map(int,i().split())))
for a in A:
    print(a, end=' ')

# 좀더 풀어쓰기
import sys
i = sys.stdin.readline
N,X = map(int, i().split())
def isSmallerThanX(a):
    return a<X
A = list(map(int,i().split()))
List = list(filter(isSmallerThanX,A))
for a in List:
    print(a, end=' ')

# for문 사용하지 않고 풀기
import sys
i = sys.stdin.readline
N,X = map(int,i().split())
A = list(filter(lambda a: a< X,map(int,i().split())))
print(*A, sep=' ')