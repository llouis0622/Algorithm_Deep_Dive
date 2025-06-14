n = int(input())
temp = input()
prefix, suffix = temp.split('*')
for _ in range(n):
    ans = input()
    if len(ans) < len(prefix) + len(suffix):
        print("NE")
        continue
    if ans.startswith(prefix) and ans.endswith(suffix):
        print("DA")
    else:
        print("NE")