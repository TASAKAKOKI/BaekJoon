'''
사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다. 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다. 게임 룰은 다음과 같다.

1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.

그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.
.....
두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다.

다음은 4명이 카드를 비교하는 경우로, 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다. 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는 바꾸지 않는다.
            2
        ↗     ↖
      1          2
    ↗  ↖     ↗  ↖
  1       3   2     1
  1       2   3     4
N명이 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만드시오.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 인원수 N과 다음 줄에 N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100
카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 1등의 번호를 출력한다.

입력
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3	 

출력
#1 3
#2 5
#3 1
'''

'''
# 0 DFS시도했으나, 분할정복이 더 나은 방법인듯...  using sys.stdin
import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Stack2/input_4880.txt", "r")
def compare(A,B):
  if A == 3:
    if B != 1:
      return True
    else:
      return False
  else:
    if B != A + 1:
      return True
    else:
      return False

def checkWinner(List):
  if len(List) == 1:
    return
  ls = [List]
  global Winner
  Winner = []
  while ls:
    A = ls.pop()
    S = 0
    E = len(A) - 1
    M = (S + E) // 2
    if len(A) > 2:
      A, B = A[:M+1], A[M+1:]
      ls.append(B)
      ls.append(A)
    elif len(A) == 2:
      if compare(A[0][1],A[1][1]):
        Winner.append(A[0])
      else:
        Winner.append(A[1])
    else:
      Winner.append(A[0])
  checkWinner(Winner)

T =int(sys.stdin.readline())
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    cards = list(map(int,sys.stdin.readline().strip().split()))
    numberCard = [(i+1,cards[i]) for i in range(N)]
    Winner = []
    checkWinner(numberCard)
    # print('finished')
    # print(Winner)
    result = Winner[0][0]
    print(f'#{tc} {result}')
'''



import sys
sys.stdin = open("./SW_Expert_Academy/강의/Programming Intermediate/파이썬SW문제해결기본_Stack2/input_4880.txt", "r")
def compare(A,B):
  if cards[A-1] == 3:
    if cards[B-1] != 1:
      return A
    else:
      return B
  else:
    if cards[B-1] != cards[A-1] + 1:
      return A
    else:
      return B
def figureWinner(S,E):
  if S==E:
    return S
  else:
    print('current S,E:',S,E)
    Left = figureWinner(S,(S+E)//2)
    Right = figureWinner((S+E)//2+1,E)
  return compare(Left,Right)

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    cards = list(map(int,sys.stdin.readline().strip().split()))
    S = 1
    E = N
    result = figureWinner(S,E)
    print(f'#{tc} {result}')

# 1 (성공)) using input()
def compare(A,B):
  if cards[A-1] == 3:
    if cards[B-1] == 1:
      return B
    else:
      return A
  else:
    if cards[B-1] == cards[A-1] + 1:
      return B
    else:
      return A
def figureWinner(S,E):
  if S==E:
    return S
  else:
    Left = figureWinner(S,(S+E)//2)
    Right = figureWinner((S+E)//2+1,E)
  return compare(Left,Right)

T = int(input())
for tc in range(1, T+1):
  N = int(input())
  cards = list(map(int,input().split()))
  S = 1
  E = N
  print(f'#{tc} {figureWinner(S,E)}')