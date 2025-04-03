from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

V, E = map(int, stdin.readline().split())

graph = []
parent = [i for i in range(V+1)]
r = 0

for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    a, b = min(a, b), max(a, b)
    graph.append((c, a, b))
graph.sort(reverse=True)

def union_parent(a, b):
    a, b = get_parent(a), get_parent(b)
    parent[max(a, b)] = min(a, b)

def get_parent(x):
    if x == parent[x] : return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

while graph:
    c, a, b = graph.pop()
    if same_parent(a,b) : continue
    union_parent(a, b)
    r += c
    

print(r)
