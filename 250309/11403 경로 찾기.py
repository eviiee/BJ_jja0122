from sys import stdin
from collections import deque

N = int(stdin.readline())
G = [list(map(int, stdin.readline().split())) for _ in range(N)]
R = []

def search(x : int):
    global N,G
    
    q = deque([x])
    V = [0] * N

    while q:
        a = q.popleft()
        for b in range(N):
            if G[a][b] and not V[b]:
                V[b] = 1
                q.append(b)

                if not G[x][b] : G[x][b] = 1

    return V

for i in range(N):
    print(*search(i))