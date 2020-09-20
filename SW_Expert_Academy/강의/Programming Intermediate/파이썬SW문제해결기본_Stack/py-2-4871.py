'''
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9	 

출력
#1 1
#2 1
#3 1
'''

# 0 using sys.stdin
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Stack/input_4871.txt", "r")
T = sys.stdin.readline()
# print(type(T.strip()))
for tc in range(1, int(T)+1):
    V,E = map(int,sys.stdin.readline().strip().split())
    print('V is:',V,'and E is:',E)
    NodesLinking = {'{}'.format(i) : 'none' for i in range(1,V+1)}
    for j in range(E):
        start,end = map(str,sys.stdin.readline().strip().split())
        print(start,end)
        if NodesLinking[start] == 'none':
            NodesLinking[start] = end
        else:
            NodesLinking[start].append(end)
    # print(NodesLinking[1])
    print(NodesLinking)

    # print(f'#{tc} {result}')
'''
# 1 using input()
T = int(input())
for tc in range(1, T+1):
    N = list(input())
    stack = []
    result = 1
    for i in range(len(N)):
        ele = N[i]
        if ele == '(' or ele == '{':
            print(f'{i}th ele is {ele} and will be added to stack')
            stack.append(ele)
        elif ele == ')' or ele == '}':
            if len(stack) == 0:
                result = 0
                break
            else:
                print(f'{i}th ele is {ele} and we will check if added to stack')
                last = stack[-1]
                if last == '(' and ele == ')':
                    print(f'    last element is matched!: {last}')
                    stack.pop()
                elif last == '{' and ele == '}':
                    print(f'    last element is matched!: {last}')
                    stack.pop()
                else:
                    print(f'    last element not matched!: {last}')
                    result = 0
                    break
        else:
            print(f'{i}th ele is {ele}.. uhm... let\'s skip this')
            continue
    print(f'length of stack : {len(stack)}, and result is {result}')
    if len(stack) != 0:
        result = 0
    print(f'#{tc} {result}')
'''