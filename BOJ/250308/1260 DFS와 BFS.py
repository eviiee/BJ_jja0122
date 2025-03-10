from sys import stdin
from collections import deque

stdin = open('input.txt')

N, M, I = map(int, stdin.readline().split())
G = [[False] * (N+1) for _ in range(N+1)]
V = [False] * (N+1)

for adj in stdin.readlines():
    a, b = map(int, adj.split())
    G[a][b], G[b][a] = True, True

def dfs(a : int):

    global N,I,G,V

    V[a] = True
    r = [a]
    for b in range(1, N+1):
        if G[a][b] and not V[b]:
            r.extend(dfs(b))

    return r

def bfs():

    global N,I,G,V
    r = []
    V = [False] * (N+1)
    V[I] = True
    q = deque([I])

    while q:
        x = q.popleft()
        r.append(x)
        for y in range(1, N+1):
            if G[x][y] and not V[y]:
                V[y] = True
                q.append(y)

    return r

print(*dfs(I))
print(*bfs())