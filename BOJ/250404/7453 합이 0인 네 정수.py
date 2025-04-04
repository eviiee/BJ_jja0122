from itertools import chain
from collections import defaultdict
from sys import stdin

N = int(input())
A, B, C, D = [], [], [], []
ap = [A, B, C, D]
for _ in range(N):
    for i, n in enumerate(map(int, stdin.readline().split())):
        ap[i].append(n)

ab = defaultdict(int)
cd = {}
for i in range(N):
    for j in range(N):
        ab[A[i] + B[j]] += 1
        x = C[i] + D[j]
        if not x in cd: cd[x] = 0
        cd[x] += 1

r = 0
for x, c in ab.items():
    if -x in cd:
        r += c * cd[-x]
print(r)