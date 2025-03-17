from sys import stdin
import heapq

N, M, X = map(int, stdin.readline().split())
graph = {i:[] for i in range(1,N+1)}
graph_r = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a, b, t = map(int, stdin.readline().split())
    graph[a].append((t,b))
    graph_r[b].append((t,a))

def dijk(st : int, graph : dict):

    INF = 1e9
    distances = [INF] * (N+1)
    distances[st] = 0
    q = [(0,st)]

    while q:
        c, a = heapq.heappop(q)
        if c > distances[a] : continue
        for cost, b in graph[a]:
            if c + cost >= distances[b] : continue
            distances[b] = c + cost
            heapq.heappush(q, (c+cost, b))
    
    return distances

print(max(r1+r2 for r1, r2 in zip(dijk(X, graph)[1::], dijk(X, graph_r)[1::])))