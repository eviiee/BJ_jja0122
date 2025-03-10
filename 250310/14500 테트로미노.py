from sys import stdin
stdin = open('input.txt')

def main():
    N, M = map(int, stdin.readline().split())
    B = [list(map(int, stdin.readline().split())) for _ in range(N)]

    r = 0

    for n in range(2):

        for i in range(N):
            for j in range(M - 3):
                s = sum(B[i][j:j+4])
                r = max(r, s)

        for i in range(N - 1):
            for j in range(M - 2):
                l = [B[x][j:j+3] for x in range(i, i+2)]
                r = max(r, getMax(l))
        
        if n == 0 :
            B = flip(B)
            N, M = M, N

    print(r)

def flip(arr : list[list[int]]) -> list[list[int]]:
    n, m = len(arr), len(arr[0])
    arr_r = [[arr[i][j] for i in range(n)] for j in range(m)]
    return arr_r

def getMax(arr : list[list[int]]) -> int:

    sub = [
        (0, 0, 1, 0),
        (0, 0, 0, 2),
        (0, 0, 0, 1),
        (0, 0, 1, 2),
        (0, 1, 0, 2),
        (0, 2, 1, 0),
        (0, 2, 1, 2),
        (1, 0, 1, 1),
        (1, 0, 1, 2),
        (1, 1, 1, 2),
    ]

    s = sum(sum(row) for row in arr)
    m = min(arr[x1][y1] + arr[x2][y2] for x1, y1, x2, y2 in sub)

    return s - m
    

if __name__ == '__main__' : main()