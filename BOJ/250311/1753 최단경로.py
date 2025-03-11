from sys import stdin
from collections import defaultdict as dd
from heapq import heappop, heappush

def main():
    V, E = map(int, stdin.readline().split())
    k = int(stdin.readline())
    inf = float('inf')
    D = [inf for _ in range(V)]
    D[k-1] = 0
    G = dd(list)
    heap = [(0,k-1)]

    for _ in range(E):
        u, v, w = map(int, stdin.readline().split())
        G[u-1].append((w, v-1))

    while heap:
        distance, current = heappop(heap)
        if D[current] > distance : continue
        for e in G[current]:
            nd = distance + e[0]
            if nd >= D[e[1]] : continue
            D[e[1]] = nd
            heappush(heap, (nd, e[1]))

    for i in range(V): print(D[i] if D[i] != inf else 'INF')

main()