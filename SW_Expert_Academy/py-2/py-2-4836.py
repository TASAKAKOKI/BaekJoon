'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.
예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
2
2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
color = 1 (빨강), color = 2 (파랑)

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2	 

출력
#1 4
#2 5
#3 7
'''

# 0
import sys
sys.stdin = open("./SW_Expert_Academy/py-2/input_4836.txt", "r")
T = sys.stdin.readline() # 3
# print(f'T is : {T.strip()}')
for tc in range(1, int(T)+1):
    Field = [[0]*10 for _ in range(10)]
    N = sys.stdin.readline() # below 3
    N = int(N)
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

