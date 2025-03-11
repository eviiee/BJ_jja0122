from sys import stdin
stdin = open('input.txt')

def main():
    N = int(stdin.readline())
    B = [list(map(int,stdin.readline().split())) for _ in range(N)]

def left(board : list[list[int]]):

    n = len(board)

    for i in range(n):
        pos = 0
        for j in range(n):
            if not board[i][j] or j == n : continue
            board[i][pos], board[i][j] = board[i][j], 0
            pos += 1



    return