import heapq
from sys import stdin

heap = []

for _ in range(int(stdin.readline())):
    x = int(stdin.readline())
    if x == 0: print(-heapq.heappop(heap) if heap else 0)
    else: heapq.heappush(heap, -x)