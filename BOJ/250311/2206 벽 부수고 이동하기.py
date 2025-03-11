from sys import stdin
from collections import deque
stdin = open('input.txt')

def main():
    N, M = map(int, stdin.readline().split())
    B = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(N)]
    V = [[[0] * M for _ in range(N)] for _ in range(2)]
    
    q = deque([(1,0,0)])
    V[1][0][0] = 1
    dc = [(1,0),(-1,0),(0,1),(0,-1)]

    while q:
        b, x, y = q.popleft()
        for dx, dy in dc:
            nx, ny = x + dx, y + dy
            if not (0<=nx<N and 0<=ny<M) : continue
            wall = B[nx][ny]
            canbreak = b
            if wall and not canbreak : continue
            elif wall : canbreak = 0
            if V[canbreak][nx][ny] : continue
            if not canbreak and V[1][nx][ny] : continue
            V[canbreak][nx][ny] = V[b][x][y] + 1
            q.append((canbreak,nx,ny))
            
    r1, r2 = V[0][-1][-1], V[1][-1][-1]

    if r1 == r2 == 0 :
        print(-1)
        return
    if r1 == 0 : r1 = r2
    print(r1)


main()