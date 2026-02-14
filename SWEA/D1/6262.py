S = input()

for i in sorted(set(S), key=S.index):
    print(f"{i},{S.count(i)}")