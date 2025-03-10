from sys import stdin
from collections import deque
stdin = open('input.txt')

N,M = map(int, stdin.readline().split())
G = {i : set() for i in range(1, N+1)}

for l in stdin.readlines():
    a, b = map(int,l.split())
    G[a].add(b)
    G[b].add(a)

r = 2**31-1
k = 0

def kv(a : int):
    global G, N, r, k
    D = [0] * (N+1)
    q = deque([a])
    while q:
        x = q.popleft()
        for y in G[x]:
            if D[y] : continue
            D[y] = D[x] + 1
            q.append(y)
    
    s = sum(D)
    if s < r:
        r = s
        k = a

for i in range(1, N+1): kv(i)
print(k)