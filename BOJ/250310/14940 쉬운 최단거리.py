from sys import stdin
from collections import deque
stdin = open('input.txt')

N, M = map(int, stdin.readline().split())
B = []
a, b = 0, 0
for x in range(N):
    r = []
    for y, v in enumerate(map(int, stdin.readline().split())):
        if v == 2 :
            a, b = x, y
        if v == 1 : r.append(-1)
        else : r.append(0)
    B.append(r)

q = deque([(a, b)])
dc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    x, y = q.popleft()
    for dx, dy in dc:
        nx, ny = x + dx, y + dy
        if not (0<=nx<N and 0<=ny<M and B[nx][ny] == -1): continue
        B[nx][ny] = B[x][y] + 1
        q.append((nx,ny))

for row in B:
    print(*row)