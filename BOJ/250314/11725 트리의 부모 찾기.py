from sys import stdin
from collections import defaultdict as dd, deque
N = int(stdin.readline())
G = dd(list)
P = [0] * (N+1)
q = deque([1])
for _ in range(1,N):
    a, b = map(int, stdin.readline().split())
    G[a].append(b)
    G[b].append(a)

while q:
    a = q.popleft()
    for b in G[a]:
        if P[b] : continue
        P[b] = a
        q.append(b)

for i in range(2, N+1): print(P[i])