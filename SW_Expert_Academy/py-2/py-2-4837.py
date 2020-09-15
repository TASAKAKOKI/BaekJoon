'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
3 6
5 15
5 10	 

출력
#1 1
#2 1
#3 0
'''

# 0
import sys
sys.stdin = open("./SW_Expert_Academy/py-2/input_4837.txt", "r")
T = sys.stdin.readline()
A = [i for i in range(1,13)]
print(A)
for tc in range(1, int(T)+1):
    N, K = map(int,sys.stdin.readline().split())
    for i in range(1<<len(A)):
    '''

    # print(f'area number(N) is : {N.strip()}')
    List = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    # print(List[0])
    # print(type(List[0][0]))
    # print(len(List))
    count = 0
    for i in range(N):
        x1 = List[i][0]
        y1 = List[i][1]
        x2 = List[i][2]
        y2 = List[i][3]
        color = List[i][4]
        for a in range(x1,x2+1):
            for b in range(y1, y2+1):
                if Field[a][b] != 0 and Field [a][b] != color:
                    Field[a][b] = 3
                    count += 1
                else: Field[a][b] = color
        # print(f'{i+1}th list of test case {tc} is :')
    # for line in Field:
    #     print(line)
    print(f'#{tc} {count}')

# 1 (성공)
T = int(input())
for tc in range(1, T+1):
    Field = [[0]*10 for _ in range(10)]
    N = int(input())
    List = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    
    for i in range(N):
        x1 = List[i][0]
        y1 = List[i][1]
        x2 = List[i][2]
        y2 = List[i][3]
        color = List[i][4]
        for a in range(x1,x2+1):
            for b in range(y1, y2+1):
                if Field[a][b] != 0 and Field [a][b] != color:
                    Field[a][b] = 3
                    count += 1
                else: Field[a][b] = color
    print(f'#{tc} {count}')

#2 (성공)
T = int(input())
for tc in range(1, T+1):
    N = int(input()) 
    List = [list(map(int,input().split())) for _ in range(N)]
    list1 = []
    list2 = []
    count = 0
    for i in range(N):
        color = List[i][4]
        for a in range(List[i][0],List[i][2]+1):
            for b in range(List[i][1],List[i][3]+1):             
                if color == 1:
                    list1.append((a,b))
                elif color == 2:
                    list2.append((a,b))
    count = 0
    if len(list1) > len(list2):
        for position in list2:
            if position in list1:
                count += 1
    else:
        for position in list1:
            if position in list2:
                count += 1    
    print(f'#{tc} {count}')

# 3 (성공)
T = int(input())
for tc in range(1, T+1):
    N = int(input()) 
    list1 = []
    list2 = []
    for i in range(N):
        x1,y1,x2,y2,c = map(int,input().split())
        for a in range(x1,x2+1):
            for b in range(y1,y2+1):   
                if c == 1:
                    list1.append((a,b))
                elif c == 2:
                    list2.append((a,b))
    count = 0
    if len(list1) > len(list2):
        for position in list2:
            if position in list1:
                count += 1
    else:
        for position in list1:
            if position in list2:
                count += 1

    print('#%s %d' % (tc,count))
'''