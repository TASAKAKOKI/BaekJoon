'''
16진수 1자리는 2진수 4자리로 표시된다.
N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.
단, 2진수의 앞자리 0도 반드시 출력한다.
예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.
0100011111111110
10 A
11 B
12 C
13 D
14 E
15 F

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100
16진수 A부터 F는 대문자로 표시된다.

출력
#1 0100011111111110
#2 01111001111000010010
#3 01000001110110100001011011001101
'''
import  sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Advanced/응용_구현1_시작하기/5185_이진수.txt", "r")
def changeToBinaryNum(X):
    oxList = [ord(i)-55 if ord(i) in range(65,71) else int(i) for i in list(X)]
    obList = []
    for i in oxList:
        ob = [0]*4
        for j in range(4):
            ob[3-j] = str(i%2)
            i //= 2
        ob = ''.join(i for i in ob)
        obList.append(ob)
    return obList
for tc in range(1,int(sys.stdin.readline())+1):
    N,X = sys.stdin.readline().strip().split()
    B = changeToBinaryNum(X)
    print('#%d'%tc,''.join(b for b in B))