list = [];
for i in range(5):
    list.append(int(input()));
sum = 0;
for i in list:
    i = int(i);
    if(i<40):
        i=40;
    sum += i;
print(sum//5);

# 1
# print(eval("+max(8,int(input())//5)"*5))

