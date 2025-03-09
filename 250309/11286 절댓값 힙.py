import heapq
from sys import stdin

L = []

for _ in range(int(stdin.readline())):
    x = int(stdin.readline())
    if x == 0 :
        if L :
            r = heapq.heappop(L)
            print(r[0] * r[1])
        else : print(0)
    else : heapq.heappush(L,(abs(x), x // abs(x)))