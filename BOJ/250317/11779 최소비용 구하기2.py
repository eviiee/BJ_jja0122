from sys import stdin
from heapq import heappop as pop, heappush as push
from collections import defaultdict as dd
stdin = open('input.txt')
read = stdin.readline

N, M = int(read()), int(read())
E = dd(list[tuple])
for _ in range(M):
    a, b, c = map(int, read().split())
    E[a].append((c, b))
st, ed = map(int, read().split())
D = [float('inf')] * (N+1)
V = [0] * (N+1)
D[st] = 0
heap = [(0, st)]
while heap:
    current_cost, current_city = pop(heap)
    if current_cost > D[current_city] : continue
    for cost, destination in E[current_city]:
        c = current_cost + cost
        if c >= D[destination] : continue
        D[destination] = c
        V[destination] = current_city
        push(heap, (c, destination))

print(D[ed])

r = [ed]
while ed != st:
    r.append(V[ed])
    ed = V[ed]
r.reverse()
print(len(r))
print(*r)