from sys import stdin
stdin = open('input.txt')
input = lambda : stdin.readline().rstrip()

sudoku = [list(map(int, list(input()))) for _ in range(9)]

def nums(r, c):
    if sudoku[r][c] > 0 : return set()
    pn = {i for i in range(1, 10)}
    for i in range(9):
        if sudoku[r][i] > 0 : pn.discard(sudoku[r][i])
        if sudoku[i][c] > 0 : pn.discard(sudoku[i][c])
    rs = r - r%3
    cs = c - c%3
    for i in range(rs, rs + 3):
        for j in range(cs, cs + 3):
            if sudoku[i][j] > 0 : pn.discard(sudoku[i][j])

    return pn

p = [[nums(r, c) for c in range(9)] for r in range(9)]

def fill(r, c):
    if len(p[r][c]) != 1 : return
    n = p[r][c].pop()
    sudoku[r][c] = n
    for i in range(9):
        p[r][i].discard(n)
        fill(r, i)
        p[i][c].discard(n)
        fill(i, c)
    rs = r - r%3
    cs = c - c%3
    for i in range(rs, rs + 3):
        for j in range(cs, cs + 3):
            p[i][j].discard(n)
            fill(i, j)

for r in range(9):
    for c in range(9):
        fill(r, c)

while 1:
    a = False
    for r in range(9):
        for c in range(9):
            if len(p[r][c]) > 1 :
                p[r][c] = {min(p[r][c])}
                fill(r, c)
                a = True
                break
        else : continue
        break
    if not a : break
            


for i in range(9):
    print(*sudoku[i], sep='')