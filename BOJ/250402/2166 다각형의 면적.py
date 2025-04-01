from sys import stdin
from math import floor

N = int(stdin.readline())
x1, y1 = map(int, stdin.readline().split())
xn, yn = x1, y1
r = 0
for i in range(N - 1):
    xt, yt = map(int, stdin.readline().split())
    r += xn * yt - yn * xt
    xn, yn = xt, yt
r += xn * y1 - yn * x1

r = floor(abs(r/2) * 10 + 0.5) / 10
print(r)