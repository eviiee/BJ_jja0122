from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split(' '))
G = {i : [] for i in range(1, N+1)}
V = [False] * (N+1)

for _ in range(M):
    a, b = map(int, stdin.readline().split(' '))
    G[a] += [b]
    G[b] += [a]

count = 0

for i in range(1, N+1):
    if V[i] : continue
    V[i] = True
    count += 1
    q = deque([i])
    while q:
        a = q.popleft()
        for b in G[a]:
            if V[b]: continue
            V[b] = True
            q.append(b)

print(count)