from sys import stdin
from collections import Counter
stdin = open('input.txt')

N, M, B = map(int, stdin.readline().split(' '))
F = []

for _ in range(N) : F.extend(list(map(int, stdin.readline().split(' '))))
F.sort()

lo = F[0]
hi = F[-1]

counter = Counter(F)

r_time = 2**31 - 1
r_height = 0

for h in range(lo, hi+1):
    fill = 0
    remove = 0
    
    for height in counter.keys():
        dh = height - h
        if dh < 0 : fill -= dh * counter[height]
        elif dh > 0 : remove += dh * counter[height]

    if remove + B - fill <0 : break

    time = 2*remove + fill
    if r_time >= time :
        r_time = time
        r_height = h

print(r_time, r_height)