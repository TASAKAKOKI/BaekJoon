T = int(input());
list = [];
for i in range(T):
    x = input().split(' ');
    a = int(x[0]);
    b = int(x[1]);
    list.append(a + b);
for r in range(len(list)):
    print(list[r]);