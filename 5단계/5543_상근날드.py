a,b,c,d,e = int(input()), int(input()), int(input()), int(input()), int(input());
print(min(a,b,c)+min(d,e)-50);

# shorter way
a,b,c,d,e = [input() for i in range(5)];
print(min(a,b,c)+min(d,e)-50);

# 1
# *p,q,r=map(int,open(0))
# print(min(p)+min(q,r)-50)