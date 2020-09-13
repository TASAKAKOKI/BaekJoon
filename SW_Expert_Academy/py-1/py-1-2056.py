T = int(input())
for t in range(1, T + 1):
    Date = input()
    Y = Date[:4]
    M = int(Date[4:6])
    D = int(Date[6:])
    L = 30;
    TF = 1;
    if not 0 < M < 13:
        TF = 0
    elif M == 2:
        L = 28
    elif M <= 7:
        if M % 2 != 0:
            L = 31
    else:
        if M % 2 == 0:
            L = 31
    if not 0 < D < L+1:
        TF = 0
    else:
        if M < 10:
            M = '0' + str(M)
        if D < 10:
            D = '0' + str(D)
    if TF == 0:
        print(f'#{t} -1')
    else:
        print(f'#{t} {Y}/{M}/{D}');