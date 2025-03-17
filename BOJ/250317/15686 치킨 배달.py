from sys import stdin
import heapq
from collections import defaultdict as d
from itertools import combinations
stdin = open('input.txt')

def solve():
    N, M = map(int, stdin.readline().split())

    chickens = []
    residences = []

    for r in range(N):
        for c, t in enumerate(map(int, stdin.readline().split())):
            if t == 1 : residences.append((r,c))
            elif t == 2 : chickens.append((r,c))

    D = d(list)

    for cr, cc in chickens:
        for rr, rc in residences:
            heapq.heappush(D[(rr,rc)],(abs(cr - rr) + abs(cc - rc), cr, cc))

    R = []

    for sel in combinations(chickens, len(chickens) - M):
        r = 0
        for l in D.values():
            info = l.copy()
            while info:
                distance, cr, cc = heapq.heappop(info)
                if (cr, cc) in sel : continue
                r += distance
                break
        R.append(r)

    print(min(R))

solve()