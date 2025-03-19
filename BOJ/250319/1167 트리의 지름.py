from sys import stdin

V = int(stdin.readline())
E = [[] for _ in range(V+1)]
for _ in range(1,V+1):
    e = list(map(int, stdin.readline().split()))
    i = e[0]
    for j in range(1, len(e) - 1, 2):
        E[i].append((e[j], e[j+1]))

def find(st:int, graph:list):
    r = (0, 0)
    q = {(st, 0)}
    V = [False] * len(graph)
    V[st] = True
    while q:
        a, c = q.pop()
        for b, d in graph[a]:
            if V[b] : continue
            V[b] = True
            if c + d > r[1] : r = (b, c + d)
            q.add((b, c + d))

    return r

print(find(find(1, E)[0], E)[1])