n = int(input())
for i in range(n):
    temp = ''
    if i % 2 == 1:
        temp += ' '
    temp += '* ' * n
    print(temp.rstrip())