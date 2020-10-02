'''
알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

[제약 사항]
문자열의 최대 길이는 200이다.

[입력]
알파벳으로 이루어진 문자열이 주어진다.

[출력]
각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.
'''
import sys 
sys.stdin = open("./SW_Expert_Academy/SW역량테스트준비/D1-D2문제풀이_기초다지기/알파벳을 숫자로 변환.txt", "r")
string = sys.stdin.readline()
print(string)
print(ord(string[0]))
print(len(string))
for i in range(len(string)):
    print(ord(string[i])-64, end=' ')


S = input()
for i in range(len(S)):
    print(ord(S[i])-64,end=' ')