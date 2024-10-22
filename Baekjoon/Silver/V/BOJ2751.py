import sys

input = sys.stdin.readline
print = sys.stdout.write


def merge_sort(s, e):
    if e - s < 1:
        return
    
    m = int(s + (e - s) / 2)
    merge_sort(s, m)
    merge_sort(m + 1, e)
    
    for i in range(s, e + 1):
        lst[i] = A[i]
        
    k = s
    idx1 = s
    idx2 = m + 1
    
    while idx1 <= m and idx2 <= e:
        if lst[idx1] > lst[idx2]:
            A[k] = lst[idx2]
            k += 1
            idx2 += 1
        else:
            A[k] = lst[idx1]
            k += 1
            idx1 += 1
            
    while idx1 <= m:
        A[k] = lst[idx1]
        k += 1
        idx1 += 1
        
    while idx2 <= e:
        A[k] = lst[idx2]
        k += 1
        idx2 += 1


N = int(input())
A = [0] * int(N + 1)
lst = [0] * int(N + 1)

for i in range(1, N + 1):
    A[i] = int(input())
    
merge_sort(1, N)

for i in range(1, N + 1):
    print(str(A[i]) + '\n')