import sys

N = list(map(int, sys.stdin.readline().rstrip()))
L = [0] * 10
for i in N:
    if i == 6 or i == 9:
        if L[6] <= L[9]:
            L[6] += 1
        else:
            L[9] += 1
    else:
        L[i] += 1
print(max(L))
'''
https://www.acmicpc.net/problem/1475

숫자가 나오는 것마다 리스트에 1씩 더해줌
6, 9는 뒤집어서 사용 가능함 -> 리스트에 넣을 때 6과 9 인덱스를 비교하여 적은 곳에 1씩 추가
이후 전체 리스트에서 제일 큰 값을 반환
'''