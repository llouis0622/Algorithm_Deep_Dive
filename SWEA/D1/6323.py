N = int(input())


def fibo(n):
    num = [1, 1]
    for i in range(2, n):
        num.append(num[i - 1] + num[i - 2])
    print(num)


fibo(N)