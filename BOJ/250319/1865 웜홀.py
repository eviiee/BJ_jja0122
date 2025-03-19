from sys import stdin

INF = 10**7

def bf(st:int, graph:list[tuple], N:int,):
    D = [INF] * (N+1)
    D[st] = 0
    for i in range(1, N+1):
        for s, e, t in graph:
            if D[e] > D[s] + t:
                D[e] = D[s] + t
                if i == N : return True
    return False

tc = int(stdin.readline())
for _ in range(tc):
    N, M, W = map(int, stdin.readline().split())
    edge = [[INF] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        s, e, t = map(int, stdin.readline().split())
        edge[s][e] = min(edge[s][e], t)
        edge[e][s] = min(edge[e][s], t)
    for _ in range(W):
        s, e, t = map(int, stdin.readline().split())
        edge[s][e] = min(edge[s][e], -t)

    graph = set()

    for i in range(1, N+1):
        for j in range(1, N+1):
            if edge[i][j] != INF: graph.add((i, j, edge[i][j]))

    if bf(1, graph, N): print('YES')
    else: print('NO')