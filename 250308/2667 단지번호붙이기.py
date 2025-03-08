from sys import stdin
stdin = open('input.txt')
N = int(stdin.readline())
M = [list(map(int, line.rstrip())) for line in stdin.readlines()]
V = [[False] * N for _ in range(N)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
r = []

def dfs(x:int, y:int):

    V[x][y] = True
    c = 1

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if not 0<=nx<N or not 0<=ny<N or not M[nx][ny] or V[nx][ny]: continue
        c += dfs(nx,ny)

    return c

for x in range(N):
    for y in range(N):
        if M[x][y] and not V[x][y]:
            r += [dfs(x,y)]

r.sort()
print(len(r))
print(*r, sep='\n')