sudoku = [list(map(int, list(input()))) for _ in range(9)]

def nums(r, c):
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
print(*p, sep='\n')