n = int(input())
for i in range(n * 2):
    if i % 2 == 0:
        print(('* ' * ((n + 1) // 2)).rstrip())
    else:
        print((' *' * (n // 2)).rstrip())