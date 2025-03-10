from collections import deque
from sys import stdin

M, N, H = map(int, stdin.readline().split())
T = [[list(map(int,stdin.readline().split())) for _ in range(N)] for _ in range(H)]

q = deque([])
for x, floor in enumerate(T):
    for y , row in enumerate(floor):
        for z, t in enumerate(row):
            if t == 1 : q.append((x, y, z))

dc = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
c = 0
while q:
    c += 1
    for _ in range(len(q)):
        x, y, z = q.popleft()
        for dx, dy, dz in dc:
            nx, ny, nz = x + dx, y + dy, z + dz
            if not (0<=nx<H and 0<=ny<N and 0<=nz<M) or T[nx][ny][nz] != 0: continue
            T[nx][ny][nz] = 1
            q.append((nx, ny, nz))

if any(any(0 in row for row in floor) for floor in T) : print(-1)
else : print(c - 1)