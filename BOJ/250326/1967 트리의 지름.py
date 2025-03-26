from sys import stdin

N = int(stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def find(st):
    V = [False] * (N+1)
    V[st] = True
    r = (0, 0)
    
    q = {(st, 0)}
    while q:
        a, l = q.pop()
        if l > r[1] : r = (a, l)
        for b, nl in graph[a]:
            if V[b] : continue
            V[b] = True
            q.add((b, l+nl))

    return r

print(find(find(1)[0])[1])