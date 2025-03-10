from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
T = [list(map(int, stdin.readline().split())) for _ in range(N)]
V = [[0] * M for _ in range(N)]
r = 0

q = deque([])

for x, row in enumerate(T):
    for y, t in enumerate(row):
        if t == 1:
            q.append((x, y))
            V[x][y] = 1

dc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:

    x, y = q.popleft()
    r = V[x][y]

    for dx, dy in dc:
        nx, ny = x + dx, y + dy
        if not 0<=nx<N or not 0<=ny<M or V[nx][ny] or T[nx][ny] == -1 : continue
        V[nx][ny] = V[x][y] + 1
        T[nx][ny] = 1
        q.append((nx,ny))

c = 0
for row in T:
    for t in row:
        if t == 0 : break
    else : continue
    print(-1)
    break
else :
    print(r-1)

