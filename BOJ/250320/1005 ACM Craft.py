from sys import stdin
from collections import deque

for _ in range(int(stdin.readline())):

    N, K = map(int, stdin.readline().split())
    T = [0] + list(map(int, stdin.readline().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    for _ in range(K):
        X, Y = map(int, stdin.readline().split())
        graph[X].append(Y)
        indegree[Y] += 1

    q = deque([])
    D = [0] * (N+1)
    for i in range(1, N+1):
        if indegree[i] == 0 :
            q.append(i)
            D[i] = T[i]
    
    while q:
        a = q.popleft()
        for b in graph[a]:
            D[b] = max(D[b], D[a] + T[b])
            indegree[b] -= 1
            if not indegree[b] :
                q.append(b)

    W = int(stdin.readline())
    print(D[W])

