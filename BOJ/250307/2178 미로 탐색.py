from sys import stdin
from collections import deque
stdin = open('input.txt')

N, M = map(int, stdin.readline().split())
maze = [list(map(int, line.rstrip())) for line in stdin.readlines()]
V = [[0] * M for i in range(N)]
V[0][0] = 1

q = deque([(0,0)])
dc = [(0, -1), (0, 1), (1, 0), (-1, 0)]

while q:
    a, b = q.popleft()
    for dx, dy in dc:
        nx, ny = a + dx, b + dy
        if not 0<=nx<N or not 0<=ny<M or V[nx][ny] or not maze[nx][ny]: continue
        V[nx][ny] = V[a][b] + 1
        if nx == N-1 and ny == M-1 :
            q.clear()
            break
        q.append((nx, ny))
        
print(V[N-1][M-1])