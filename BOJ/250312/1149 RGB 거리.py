from sys import stdin

n = int(stdin.readline())
r, g, b = map(int, stdin.readline().split())
for i in range(1, n):
    x, y, z = map(int, stdin.readline().split())
    r, g, b = min(g, b) + x, min(r, b) + y, min(r, g) + z
print(min(r,g,b))