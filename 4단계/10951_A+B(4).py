import sys
while True:
    try:
        A,B = map(int,sys.stdin.readline().split());
        print(A+B)
    except:
        break;

# 
import sys
try:
    while True:
        A,B = map(int,sys.stdin.readline().split());
        print(A+B)
except:
    exit();

#
import sys
for line in sys.stdin:
    A,B = map(int,line.split());
    print(A+B);