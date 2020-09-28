'''
N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.
1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.
주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.

- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 화덕의 크기 N과 피자 개수 M이 주어지고, 다음 줄에 M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci가 주어진다.
3<=N<=20, N<=M<=100, 1<=Ci<=20

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.
 
입력
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2	 

출력
#1 4
#2 8
#3 6
'''

# 첫시도 10개 중 4개만 정답

'''
    # 0 using sys.stdin
    import sys
    sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Queue1/input_5099.txt", "r")

    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        N,M = map(int,sys.stdin.readline().strip().split())
        leftPizzas = list(map(int,sys.stdin.readline().strip().split()))
        # print(leftPizzas)
        for i in range(M):
            leftPizzas[i] = [(i+1),leftPizzas[i]] 
        # print(leftPizzas)
        Q = []
        result = 0
        while len(Q) != N:
            Q.append(leftPizzas.pop(0))
        while len(Q) != 1:
            # print(len(Q))
            for i in range(len(Q)):
                if len(Q)-1 < i:
                    break
                else:
                    Q[i][1] //=2
                    if Q[i][1] == 0:
                        if len(leftPizzas) != 0:
                            Q[i] = leftPizzas.pop(0)
                        else:
                            Q.pop(i)
                            if len(Q) == 1:
                                break
                # print(Q)
        print(f'#{tc} {Q.pop(0)[0]}')
'''

'''
    # 1 using input
    T = int(input())
    for tc in range(1, T+1):
        N,M = map(int,input().split())
        leftPizzas = list(map(int,input().split()))
        for i in range(M):
            leftPizzas[i] = [(i+1),leftPizzas[i]] 
        Q = []
        result = 0
        while len(Q) != N:
            Q.append(leftPizzas.pop(0))
        while len(Q) != 1:
            for i in range(len(Q)):
                if len(Q)-1 < i:
                    break
                else:
                    Q[i][1] //=2
                    if Q[i][1] == 0:
                        if len(leftPizzas) != 0:
                            Q[i] = leftPizzas.pop(0)
                        else:
                            Q.pop(i)
                            if len(Q) == 1:
                                break
        print(f'#{tc} {Q.pop(0)[0]}')
'''

# 0 using sys.stdin
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Queue1/input_5099.txt", "r")

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N,M = map(int,sys.stdin.readline().strip().split())
    # L은 화덕에 들어갈 피자들의 대기열.
    L = list(map(int,sys.stdin.readline().strip().split()))
    # L에 현재는 각 피자별 치즈의 양만 있으므로, 각 함수에 피자 번호를 함께  [피자번호, 치즈의 양]과 같이 리스트로 저장. --> 더 나은 방법 있을 것.
    for i in range(M):
        L[i] = [(i + 1), L[i]] 
    # Q는 화덕으로써, 앞에서 주어진 크기 N만큼의 자리를 갖는 리스트(화덕) 생성.
    Q = [0] * N

    # F는 화덕의 입구로, 화덕 안의 각 요소를 이동시키기 보다, F에 변화를 주면, 각 피자들이 돌아가는 논리적 움직임 표현 가능. 초기값은 0으로 준다
    F = 0
    cycle = 0
    while True:
        # 만약 대기중인 피자들이 아직 있다면,
        while L:
            # 화덕입구(F)에 피자가 없다면 L의 맨 앞 피자를 빼서 넣어준다.
            if Q[F] == 0:
                Q[F] = L.pop(0)
                # 피자를 넣어주면서 치즈의 양이 반으로 줄어든 상태로 만들어 준다.
                Q[F][1] //= 2
                # 화덕의 입구를 한칸 이동한다.(피자들이 화덕 안에서 돌아간 것)
                F = (F+1) % N

            # 화덕입구(F)에 피자가 있다면, 치즈 상태 확인.
            else:
                # 치즈가 남아있다면, 반으로 줄이고 화덕 입구 이동
                if Q[F][1] != 0:
                    Q[F][1] //= 2
                    F =(F+1) % N
                # 만약 치즈가 사라져 있다면, 피자를 빼준다.
                else:
                    Q[F] = 0
        if Q[F][1] != 0:
            Q[F][1] //= 2
        else:
            cycle +=1
        F =(F+1) % N
        if cycle == N-1:
            break
    print(Q)
    # print(f'#{tc} {Q.pop(0)[0]}')