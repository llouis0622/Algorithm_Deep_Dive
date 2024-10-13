from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline

N = int(input())
pq = PriorityQueue()

for i in range(N):
    num = int(input())

    if num == 0:
        if pq.empty():
            print('0\n')
        else:
            idx = pq.get()
            print(str((idx[1])) + '\n')
    else:
        pq.put((abs(num), num))