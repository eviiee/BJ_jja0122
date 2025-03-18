from sys import stdin

def main():
    V, E = map(int, stdin.readline().split())
    G = {i:[] for i in range(1, V+1)}
    for _ in range(E):
        a, b, c = map(int, stdin.readline().split())
        G[a].append((c, b))
        G[b].append((c, a))
    v1, v2 = map(int, stdin.readline().split())
    try:
        r1 = sum([
            dijk(1, v1, G, V),
            dijk(v1, v2, G, V),
            dijk(v2, V, G, V),
        ])
        r2 = sum([
            dijk(1, v2, G, V),
            dijk(v2, v1, G, V),
            dijk(v1, V, G, V),
        ])
        print(min(r1, r2))
    except:
        print(-1)

    
def dijk(st: int, ed: int, graph: dict, V: int):

    import heapq

    INF = float('inf')
    distance = [INF] * (V+1)
    distance[st] = 0
    heap = [(0, st)]

    while heap:
        dist, v = heapq.heappop(heap)
        if distance[v] < dist : continue
        if v == ed : return dist
        for d, nxt in graph[v]:
            if dist + d >= distance[nxt]: continue
            distance[nxt] = dist + d
            heapq.heappush(heap, (dist + d, nxt))

    else: raise Exception

if __name__ == '__main__' : main()