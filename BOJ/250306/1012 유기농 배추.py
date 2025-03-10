from sys import stdin, setrecursionlimit
stdin = open('input.txt')

def main():
    for _ in range(int(stdin.readline())):
        M, N, K = map(int, stdin.readline().split(' '))
        F = [[0] * N for _ in range(M)]
        for _ in range(K):
            x, y = map(int, stdin.readline().split(' '))
            F[x][y] = 1
        print(count(F))

def count(field : list):

    M = len(field)
    N = len(field[0])

    V = [[False] * N for _ in range(M)]

    c = 0

    def dfs(a : int, b : int):
        V[a][b] = True
        if a > 0 and field[a-1][b] == 1 and not V[a-1][b] : dfs(a-1,b)
        if a < M-1 and field[a+1][b] == 1 and not V[a+1][b] : dfs(a+1,b)
        if b > 0 and field[a][b-1] == 1 and not V[a][b-1] : dfs(a,b-1)
        if b < N-1 and field[a][b+1] == 1 and not V[a][b+1] : dfs(a,b+1)

    for x, row in enumerate(field):
        for y, v in enumerate(row):
            if v == 0 or V[x][y]: continue
            c += 1
            dfs(x, y)

    return c

setrecursionlimit(10**6)
main()