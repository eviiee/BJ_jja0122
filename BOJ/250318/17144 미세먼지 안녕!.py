from sys import stdin
stdin = open('input.txt')

R, C, T = map(int, stdin.readline().split())
room = [list(map(int, stdin.readline().split())) for _ in range(R)]
TT = 0
P1, P2 = 0, 0

def init():
    global P1, P2
    for i in range(R):
        if room[i][0] == -1 :
            P1, P2 = i, i+1
            return

def diffuse():
    diff = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] <= 0 : continue
            count = 0
            d = room[r][c] // 5
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if not (0<=nr<R and 0<=nc<C and room[nr][nc] >= 0) : continue
                count+=1
                diff[nr][nc] += d
            room[r][c] -= d * count
    for i in range(R):
        for j in range(C):
            room[i][j] += diff[i][j]
    return

def circulate():
    for r in range(P1 -1, 0, -1): room[r-1][0], room[r][0] = 0, room[r-1][0]
    for r in range(P2 + 1, R - 1): room[r+1][0], room[r][0] = 0, room[r+1][0]
    for c in range(C-1):
        room[0][c], room[0][c+1] = room[0][c+1], 0
        room[-1][c], room[-1][c+1] = room[-1][c+1], 0
    for r in range(P1): room[r][-1], room[r+1][-1] = room[r+1][-1], 0
    for r in range(R-1, P2, -1): room[r][-1], room[r-1][-1] = room[r-1][-1], 0
    for c in range(C-1, 1, -1):
        room[P1][c], room[P1][c-1] = room[P1][c-1], 0
        room[P2][c], room[P2][c-1] = room[P2][c-1], 0
    return

def main():
    init()
    for _ in range(T):
        diffuse()
        circulate()
    r = sum(sum(row) for row in room) + 2
    print(r)
    return

if __name__ == '__main__' : main()