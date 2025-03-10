from collections import deque
from sys import stdin
stdin = open('input.txt')
def main():
    n = int(stdin.readline())
    B = [list(stdin.readline().rstrip()) for _ in range(n)]
    V = [[False] * n for _ in range(n)]
    greens = []

    c1, c2 = 0, 0
    for i in range(n):
        for j in range(n):
            if B[i][j] == 'G' : greens.append((i,j))
            if V[i][j]: continue
            if B[i][j] == 'B': c1 += 1
            else : c2 += 1
            bfs(i,j,B,V)
    
    c3 = 0
    for i, j  in greens: B[i][j] = 'R'
    V = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if V[i][j] or B[i][j] != 'R' : continue
            c3 += 1
            bfs(i,j,B,V)

    print(c1+c2, c1+c3)

def bfs(a:int, b:int, B:list[list[str]], V:list[list[bool]]):
    q = deque([(a,b)])
    V[a][b] = True
    c = B[a][b]
    n = len(B)
    delta = ((0,1),(0,-1),(1,0),(-1,0))

    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx,ny = x + dx, y + dy
            if not (0<=nx<n and 0<=ny<n and B[nx][ny] == c) or V[nx][ny] : continue
            V[nx][ny] = True
            q.append((nx,ny))

if __name__ == '__main__' : main()