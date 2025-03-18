import heapq
from sys import stdin
stdin = open('input.txt')

INF = float('inf')
N, M, R = map(int, stdin.readline().split())
items = list(map(int, stdin.readline().split()))
G = [[INF] * N for _ in range(N)]
for i in range(N): G[i][i] = 0
for _ in range(R):
    a, b, l = map(int, stdin.readline().split())
    G[a-1][b-1], G[b-1][a-1] = l, l

for k in range(N):
    for i in range(N):
        for j in range(i+1, N):
            G[i][j] = min(G[i][k] + G[k][j], G[i][j])
            G[j][i] = G[i][j]

R = [0] * N
for i in range(N):
    for j in range(N):
        if G[i][j] <= M : R[i] += items[j]

print(max(R))