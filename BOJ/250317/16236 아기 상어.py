from collections import deque
from sys import stdin

stdin = open('input.txt')

N = int(stdin.readline())
aquarium = [list(map(int, stdin.readline().split())) for _ in range(N)]
current_r, current_c, size, exp = 0, 0, 2, 0

def main():
    global size, exp, current_c,current_r
    r = 0
    findShark()
    try:
        while True:
            r += hunt()
            exp += 1
            if size == exp :
                size += 1
                exp = 0
    except:
        print(r)

def findShark():

    global current_r, current_c
    for r, row in enumerate(aquarium):
        for c, v in enumerate(row):
            if v == 9 :
                aquarium[r][c] = 0
                current_r, current_c = r, c
                return

def hunt():
    global current_r, current_c
    V = [[False] * N for _ in range(N)]
    V[current_r][current_c] = True
    q = deque([(current_r, current_c)])
    distance = 0

    h = False
    fx, fy = N, N

    while q:
        distance += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in ((-1, 0),(0, -1),(0,1),(1,0)):
                nx, ny = x+dx, y+dy
                if not (0<=nx<N and 0<=ny<N) or V[nx][ny] : continue
                if aquarium[nx][ny] > size : continue
                V[nx][ny] = True
                if 0 < aquarium[nx][ny] < size :
                    h = True
                    if nx < fx : fx, fy = nx, ny
                    elif nx == fx : fy = min(ny, fy)
                    else : continue
                q.append((nx, ny))
        if h :
            current_r, current_c = fx, fy
            aquarium[fx][fy] = 0
            return distance
    else : raise Exception

if __name__ == '__main__' : main()