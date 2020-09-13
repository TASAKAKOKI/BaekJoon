T = int(input())
list = list(map(int,input().split()))
print(sorted(list)[int((T-1)/2)])
