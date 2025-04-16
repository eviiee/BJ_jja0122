from sys import stdin
input = lambda : stdin.readline().rstrip()
stdin = open('input.txt')
R, C, K = map(int, input().split())

M = [list(input()) for _ in range(R)]
V = [[False] * C for _ in range(R)]
V[R-1][0] = True

v = 0
def dfs(r, c, d):
    global v

    if d > K : return
    if r == 0 and c == C - 1 :
        if K == d : v += 1
        return
    
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if not (0<=nr<R and 0<=nc<C) or V[nr][nc] or M[nr][nc] == 'T' : continue
        V[nr][nc] = True
        dfs(nr, nc, d + 1)
        V[nr][nc] = False
    
    return

dfs(R-1, 0, 1)
print(v)
    