from collections import deque
from sys import stdin

stdin = open('input.txt')

def bfs():
    global N, M, C

    ix, iy = 0, 0

    for i, row in enumerate(C):
        for j, t in enumerate(row):
            if t == 'I' :
                ix = i
                iy = j
                C[i][j] = 'V'

    q = deque([(ix, iy)])
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)

    count = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0>nx or 0>ny or N<=nx or M<=ny : continue
            t = C[nx][ny]
            if t in 'VX': continue
            if t == 'P' : count+=1
            C[nx][ny] = 'V'
            q.append((nx, ny))
    
    print(count if count > 0 else 'TT')



N, M = map(int, stdin.readline().split(' '))
C = [list(row.rstrip()) for row in stdin.readlines()]

bfs()