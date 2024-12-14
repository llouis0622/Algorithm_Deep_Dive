import math

N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())
sizes = [S, M, L, XL, XXL, XXXL]
total_tshirts = sum(math.ceil(size / T) for size in sizes)
pen_bundles = N // P
remaining_pens = N % P
print(total_tshirts)
print(pen_bundles, remaining_pens)