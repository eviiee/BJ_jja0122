from itertools import combinations
from collections import deque
from sys import stdin
from copy import deepcopy


virus = []
empty = []

def bfs(walls):
    m = deepcopy(room)
    for x, y in walls : m[x][y] = 1
    q = deque(virus)

    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if not (0<=nx<N and 0<=ny<M) or m[nx][ny] : continue
            m[nx][ny] = 2
            q.append((nx,ny))
    s = 0
    for i in range(N):
        for j in range(M):
            if m[i][j] == 0 : s += 1

    return s

N, M = map(int, stdin.readline().split())
room = [list(map(int, stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if room[i][j] == 2 : virus.append((i,j))
        elif room[i][j] == 0 : empty.append((i,j))

r = 0
for comb in combinations(empty, 3):
    r = max(r, bfs(comb))
print(r)