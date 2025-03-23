from sys import stdin

C = {
    'R' : [1, 0],
    'L' : [-1, 0],
    'B' : [0, -1],
    'T' : [0, 1],
}

p = lambda x : list(map(ord, x))
v = lambda x, y : 65<=x<=72 and 49<=y<=56

king, stone, N = stdin.readline().split()
king, stone, N = p(king), p(stone), int(N)

for _ in range(N):
    dx, dy = [sum(x) for x in zip(*[C[c] for c in stdin.readline().rstrip()])]
    kx, ky = king
    kx, ky = kx + dx, ky + dy
    sx, sy = stone
    if kx == sx and ky == sy : sx, sy = sx + dx, sy + dy

    if v(kx, ky) and v(sx, sy) :
        king[0], king[1] = kx, ky
        stone[0], stone[1] = sx, sy

print(*[chr(x) for x in king], sep='')
print(*[chr(x) for x in stone], sep='')