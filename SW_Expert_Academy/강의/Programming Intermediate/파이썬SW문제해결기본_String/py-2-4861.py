'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
20 13
ECFQBKSYBBOSZQSFBXKI
VBOAIDLYEXYMNGLLIOPP
AIZMTVJBZAWSJEIGAKWB
CABLQKMRFNBINNZSOGNT
NQLMHYUMBOCSZWIOBINM
QJZQPSOMNQELBPLVXNRN
RHMDWPBHDAMWROUFTPYH
FNERUGIFZNLJSSATGFHF
TUIAXPMHFKDLQLNYQBPW
OPIRADJURRDLTDKZGOGA
JHYXHBQTLMMHOOOHMMLT
XXCNJGTXXKUCVOUYNXZR
RMWTQQFHZUIGCJBASNOX
CVODFKWMJSGMFTCSLLWO
EJISQCXLNQHEIXXZSGKG
KGVFJLNNBTVXJLFXPOZA
YUNDJDSSOPRVSLLHGKGZ
OZVTWRYWRFIAIPEYRFFG
ERAPUWPSHHKSWCTBAPXR
FIKQJTQDYLGMMWMEGRUZ	 

출력
#1 JAEZNNZEAJ
#2 MWOIVVIOWM
#3 TLMMHOOOHMMLT
'''

# 0 with comments
import sys,math
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_String/input_4861.txt", "r")
T = sys.stdin.readline()
# print(T.strip())
for tc in range(1, int(T)+1):
    N,M = map(int,sys.stdin.readline().strip().split())
    # print(N,M)
    List = [sys.stdin.readline().strip() for i in range(N)]
    # print(List)
    result = ''
    for i in range(N):
        j = 0
        wholeRow = []
        while j <= N-M:
            out = ''.join(list(List[i][k] for k in range(j,M+j)))
            wholeRow.append(out)
            j += 1
        # print(wholeRow)
        for word in wholeRow:
            if word[:M//2][::-1] == word[math.ceil(M/2):]:
                result = word
                break
        if result:
            break
        wholeCol = []
        l = 0
        while l <= N-M:
            out = ''.join(list(List[k][i] for k in range(l,M+l)))
            wholeCol.append(out)
            l += 1
        # print(wholeCol)
        for word in wholeCol:
            if word[:M//2][::-1] == word[math.ceil(M/2):]:
                result = word
    print('#%d'%tc, result)

# 0-1 without comment
import sys,math
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_String/input_4861.txt", "r")
T = sys.stdin.readline()
for tc in range(1, int(T)+1):
    N,M = map(int,sys.stdin.readline().strip().split())
    List = [sys.stdin.readline().strip() for i in range(N)]
    result = ''
    for i in range(N):
        j = 0
        wholeRow = []
        while j <= N-M:
            out = ''.join(list(List[i][k] for k in range(j,M+j)))
            wholeRow.append(out)
            j += 1
        for word in wholeRow:
            if word[:M//2][::-1] == word[math.ceil(M/2):]:
                result = word
                break
        if result:
            break
        wholeCol = []
        l = 0
        while l <= N-M:
            out = ''.join(list(List[k][i] for k in range(l,M+l)))
            wholeCol.append(out)
            l += 1
        for word in wholeCol:
            if word[:M//2][::-1] == word[math.ceil(M/2):]:
                result = word
    print('#%d'%tc, result)

# 1 (성공)
import math
T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    List = [input() for i in range(N)]
    result = ''
    for i in range(N):
        j = 0
        wholeRow = []
        while j <= N-M:
            out = ''.join(list(List[i][k] for k in range(j,M+j)))
            wholeRow.append(out)
            j += 1
        for word in wholeRow:
            if word[:M//2][::-1] == word[math.ceil(M/2):]:
                result = word
                break
        if result:
            break
        wholeCol = []
        l = 0
        while l <= N-M:
            out = ''.join(list(List[k][i] for k in range(l,M+l)))
            wholeCol.append(out)
            l += 1
        for word in wholeCol:
            if word[:M//2][::-1] == word[math.ceil(M/2):]:
                result = word
    print('#%d'%tc, result)

'''
seqList = [1, 2, 4, 3, 5]
print(reversed(seqList))
 
# [5, 3, 4, 2, 1]
 
array=[0, 10, 20, 40]
for i in reversed(array):
    print(i)
'''