import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
X = int(sys.stdin.readline())
L.sort()
cnt, start, end = 0, 0, len(L) - 1
while start < end:
    if L[start] + L[end] > X:
        end -= 1
    elif L[start] + L[end] < X:
        start += 1
    else:
        cnt += 1
        start += 1
        end -= 1
print(cnt)
'''
리스트로 저장 후 정렬 -> 투 포인터를 쓰기 위함
start와 end의 합을 비교하면서 목표값에서의 차이를 기준으로 포인터 이동
목표값과 포인터 값의 합이 같다면 cnt 증가, 이후 cnt 개수 반환
'''