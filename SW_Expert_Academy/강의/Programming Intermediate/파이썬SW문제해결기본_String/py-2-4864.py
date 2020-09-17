'''
두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
ABC
ZZZZZABCZZZZZ
두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
ABC
ZZZZAZBCZZZZZ
문자열이 일치하지 않으므로 0을 출력.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW	 

출력
#1 1
#2 0
#3 1
'''

# 1-0 (성공)
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_String/input_4864.txt", "r")
T = sys.stdin.readline()
for tc in range(1, int(T)+1):
    str1 = list(sys.stdin.readline().strip())
    str2 = list(sys.stdin.readline().strip())
    print(str1)
    print(str1[-1],str2)
    #1
    # indices = []
    # for i in range(len(str2)):
    #     if str2[i] == str1[-1]:
    #         indices.append(i)
    #2
    indices = [idx for idx,val in enumerate(str2) if val == str1[-1]]
    print(indices)
    Result = 0
    if len(indices) != 0:
        for j in range(len(indices)):
            start = indices[j]-len(str1)+1
            end = indices[j]+1
            if str2[start:end] == str1:
                Result = 1
                break
    else:
        Result = 0
    print('#%d'%tc,Result)

#1-1 comment생략
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_String/input_4864.txt", "r")
T = sys.stdin.readline()
for tc in range(1, int(T)+1):
    str1 = list(sys.stdin.readline().strip())
    str2 = list(sys.stdin.readline().strip())
    indices = [idx for idx,val in enumerate(str2) if val == str1[-1]]
    Result = 0
    if len(indices) != 0:
        for j in range(len(indices)):
            start = indices[j]-len(str1)+1
            end = indices[j]+1
            if str2[start:end] == str1:
                Result = 1
                break
    else:
        Result = 0
    print('#%d'%tc,Result)

#1-2 input()사용 (성공)
T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    indices = [idx for idx,val in enumerate(str2) if val == str1[-1]]
    Result = 0
    if len(indices) != 0:
        for j in range(len(indices)):
            start = indices[j]-len(str1)+1
            end = indices[j]+1
            if str2[start:end] == str1:
                Result = 1
                break
    else:
        Result = 0
    print('#%d'%tc,Result)

'''
# 0 (일부 오답 발생)
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_String/input_4864.txt", "r")
T = sys.stdin.readline()
# print(T.strip())
for tc in range(1, int(T)+1):
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    # print(str1, type(str1), len(str1))
    # print(str2, type(str2), len(str2)) 
    len1 = len(str1)   
    i = len1 - 1
    print('last index is:',i)
    j = len1 - 1
    result = 0
    while j != 0 and i < len(str2):
        checkLetter = str2[i]
        print('\n','current checking Letter is:',checkLetter)
        print('now i is :', i)
        if checkLetter == str1[j]:
            i -= 1
            j -= 1
            print('oh last letter matched! now index is :', i)
        else:
            j = len1 - 1
            print('oppps, last letter didnt matched')
            try:
                i += len1 - 1 - str1.index(checkLetter)
                print('but last letter is within the str1')
                print('it is located at :', i-len1-1,' th place in str 1')
                print('so// now i is : ',i)
            except:
                print('uhm.....last letter is even not within the str1')
                i += len1
                print('so.. now i is : ',i)
    if j == 0:
        result = 1
    else:
        result = 0
    print('#%d'%tc,result)
'''

'''
# 0-1 without comment (일부 오답 발생)
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_String/input_4864.txt", "r")
T = sys.stdin.readline()
for tc in range(1, int(T)+1):
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    print(str1)
    count,i,j = 0,len(str1)-1, len(str1)-1   
    while i >= 0 and j < len(str2):
        if str2[j] == str1[i]:
            count = 1
            for k in range(1,len(str1)):
                if str2[j-k] == str1[i-k]:
                    count += 1
                else:
                    i = len(str1)-1
                    j += len(str1)
                    break
            if count == len(str1):
                break
        elif str2[j] in str1:
            j += len(str1)-1-str1.index(str2[j])
            i = len(str1)-1
        else:
            i = len(str1)-1
            j += len(str1)
    print(count)
    print('#%d'%tc,1 if count == len(str1) else 0)
'''

'''
# 0-2 (일부 오답 발생)
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    count,i,j = 0,len(str1)-1, len(str1)-1   
    while i >= 0 and j < len(str2):
        if str2[j] == str1[i]:
            count = 1
            for k in range(1,len(str1)):
                if str2[j-k] == str1[i-k]:
                    count += 1
                else:
                    i = len(str1)-1
                    j += len(str1)
                    break
            if count == len(str1):
                break
        elif str2[j] in str1:
            j += len(str1)-1-str1.index(str2[j])
            i = len(str1)-1
        else:
            i = len(str1)-1
            j += len(str1)
    print('#%d'%tc,1 if count == len(str1) else 0)
'''