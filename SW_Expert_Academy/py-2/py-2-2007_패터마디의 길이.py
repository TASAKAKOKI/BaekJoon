# 0
import sys
sys.stdin = open("./SW_Expert_Academy/py-2/2007.txt", "r")
T = int(sys.stdin.readline())
for tc in range(1,T+1):
    Str = sys.stdin.readline().strip()
    stack = []
    for j in range(30):
        result = 0
        while True:
            if len(stack)!= 0 and stack[0] == Str[j]:
                result += 1
                for k in range(1,30-j):
                    try:
                        if stack[k] == Str[j+k]:
                            result += 1
                        else:
                            stack.append(Str[j])
                            break
                    except:
                        break
                break
            else:
                stack.append(Str[j])
                break
        if result > 1:
            break
    print('#%d'%tc,result)

# 1
T = int(input())
for tc in range(1,T+1):
    Str = input()
    stack = []
    for j in range(30):
        result = 0
        while True:
            if len(stack)!= 0 and stack[0] == Str[j]:
                result += 1
                for k in range(1,30-j):
                    try:
                        if stack[k] == Str[j+k]:
                            result += 1
                        else:
                            stack.append(Str[j])
                            break
                    except:
                        break
                break
            else:
                stack.append(Str[j])
                break
        if result > 1:
            break
    print('#%d'%tc,result)