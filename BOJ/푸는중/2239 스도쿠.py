from sys import stdin
stdin = open('input.txt')
input = lambda : stdin.readline().rstrip()

initial = []
sudoku = []
empty = []

def init():
    global sudoku, empty, initial
    sudoku = [list(map(int, list(input()))) for _ in range(9)]
    from copy import deepcopy
    initial = deepcopy(sudoku)
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 : empty.append([(i, j), nums(i,j)])

    print(*empty, sep='\n')

def check(r, c):
    pos = set()
    for i in range(9):
        pos.add((r, i))
        pos.add((i, c))
        pos.add((r - r%3 + i//3, c - c%3 + i%3))
    return pos

def nums(r, c):
    n = {i for i in range(10)}
    for x, y in check(r, c): n.discard(sudoku[x][y])
    return n

def fill(i):
    pos, nums = empty[i]
    r, c = pos
    n = min(nums)
    empty.pop(i)
    sudoku[r][c] = n
    dup = check(r, c)
    for x in range(len(empty)):
        if empty[x][0] in dup: empty[x][1].discard(n)

def try_fill():
    for i in range(len(empty)):
        if len(empty[i][1]) == 1:
            fill(i)
            return
        
    for i in range(len(empty)):
        if len(empty[i][1]) > 1:
            fill(i)
            return

def main():
    init()
    while empty: try_fill()
    for i in range(9):
        print(initial[i], sudoku[i])
    print(*empty,sep='\n')

if __name__ == '__main__':
    main()



# 365492718
# 849761235
# 127358964
# 712984351
# 451637892
# 983215476
# 574819623
# 234176589
# 698543137