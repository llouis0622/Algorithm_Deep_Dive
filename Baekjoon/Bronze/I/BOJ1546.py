N = int(input())
lst = list(map(int, input().split()))
num = max(lst)
ans = sum(lst)
print(ans * 100 / num / int(N))