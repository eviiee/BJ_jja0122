from sys import stdin
N, M = int(stdin.readline()), int(stdin.readline())
INF = float('inf')
graph = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, stdin.readline().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for i in range(N): graph[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    for j in range(N):
        if graph[i][j] == INF : graph[i][j] = 0
        
for row in graph: print(*row)