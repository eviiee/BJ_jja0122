from collections import deque
from sys import stdin

stdin = open('input.txt')

N, M = map(int, stdin.readline().split())
C = [list(map(int, stdin.readline().split())) for _ in range(N)]
V = [[False] * M for _ in range(N)]
melt = {(0,0)}

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
            nx, ny = x+dx, y+dy
            if not (0<=nx<N and 0<=ny<M) or V[nx][ny] : continue
            if C[nx][ny] > 0 :
                C[nx][ny] += 1
                if C[nx][ny] >= 3:
                    melt.add((nx,ny))
                continue
            V[nx][ny] = True
            q.append((nx,ny))

r = 0
while True:
    q = deque(melt)
    for x, y in melt: V[x][y] = True
    melt.clear()
    bfs()
    if not melt : break
    r += 1
print(r)