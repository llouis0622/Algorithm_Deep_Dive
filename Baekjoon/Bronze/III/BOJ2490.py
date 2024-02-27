for i in range(3):
    L = list(map(int, input().split()))
    if sum(L) == 4:
        print('E')
    elif sum(L) == 3:
        print('A')
    elif sum(L) == 2:
        print('B')
    elif sum(L) == 1:
        print('C')
    else:
        print('D')