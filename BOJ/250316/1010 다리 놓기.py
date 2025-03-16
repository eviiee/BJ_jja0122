from sys import stdin
from math import comb
for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    N, M = min(N, M), max(N, M)
    print(comb(M, M - N))

