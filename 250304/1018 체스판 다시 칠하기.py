from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split(' '))
    board = [list(input().rstrip()) for _ in range(n)]
    
    for r in range(n):
        for c in range(m):
            board[r][c] = board[r][c] == 'W'

    result = 64

    for x in range(n - 7):
        for y in range(m - 7):

            newboard = [board[r][y:y+8:] for r in range(x, x+8)]
            printMap = [[False] * 8 for _ in range(8)]
            
            for r in range(1, 8):
                if not (newboard[r-1][0] ^ newboard[r][0]):
                    printMap[r][0] = True
                    newboard[r][0] = not newboard[r][0]
            for r in range(8):
                for c in range(1,8):
                    if not (newboard[r][c-1] ^ newboard[r][c]):
                        printMap[r][c] = True
                        newboard[r][c] = not newboard[r][c]

            s = sum([sum(printMap[r]) for r in range(8)])
            result = min([s, 64 - s, result])

    print(result)

if __name__ == '__main__':
    main()