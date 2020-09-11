x,y = map(int,input().split('');
if(x==0 and y<45):
    print(f"23 {y+15}");
else:
    if(y>=45):
        print(f"{x} {y-45}");
    else:
        print(f"{x-1} {y+15}");

'''
Result
시간: 60ms
메모리: 29380KB
'''
