from collections import defaultdict as d
from sys import stdin
from heapq import heappop as pop, heappush as push

G = d(list[tuple])
N, M = int(stdin.readline()), int(stdin.readline())
C = [float('inf')] * (N+1)
for _ in range(M):
    a, b, c = map(int, stdin.readline().split())
    G[a].append((c, b))
x, y = map(int, stdin.readline().split())
q = [(0,x)]
while q:
    cc, a = pop(q)
    if cc > C[a] : continue
    for c, b in G[a]:
        tc = cc + c
        if tc >= C[b] : continue
        C[b] = tc
        push(q, (tc, b))
print(C[y])