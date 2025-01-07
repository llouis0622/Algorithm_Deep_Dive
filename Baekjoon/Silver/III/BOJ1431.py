import sys


def digit(serial):
    return sum(int(i) for i in serial if i.isdigit())


input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
lst = data[1:]
lst.sort(key=lambda x: (len(x), digit(x), x))
print("\n".join(lst))