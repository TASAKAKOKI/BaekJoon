# a,b,c = map(int,input().split());
# m = a;
# m2 = a;
# m = max(max(a,b),c);
# if m==a:
#     m2 = max(b,c);
# elif m==b:
#     m2 = max(a,c);
# elif m==c:
#     m2 = max(a,b);
# print(m2);


# list.sort()  --> return None
list = list(map(int,input().split()));
list.sort();
print(list[-2]);

# sorted(list) --> return sorted list
list = list(map(int,input().split()));
print(sorted(list)[-2]);


# 1
print(sorted(input().split(),key=int)[-2]);
