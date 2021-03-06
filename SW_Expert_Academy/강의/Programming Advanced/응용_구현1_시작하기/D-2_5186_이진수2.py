'''
0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.
N = 0.625
0.101 (이진수)
    = 1*2^(-1) + 0*2^(-2) + 1*2^(-3)
    = 0.5 + 0 + 0.125
    = 0.625
N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 소수점 아래가 12자리 이내인 N이 주어진다.

출력
#1 101
#2 overflow
#3 001
'''
import  sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Advanced/응용_구현1_시작하기/5186_이진수2.txt", "r")
def cnvtToB(N):
    Len = len(str(N))
    newN = N
    List = []
    for i in range(2,15):
        newN = newN*2
        List.append(str(int(newN)))
        newN -= int(newN)
        if len(str(newN))>14:
            return 'overflow'
        if newN == 0 or newN == 1.0:
            break
    if len(List) > 12:
        return 'overflow'
    else:
        return ''.join(i for i in List)
for tc in range(1,int(sys.stdin.readline())+1):
    N = float(sys.stdin.readline())
    result = cnvtToB(N)
    print('#%d'%tc,result)