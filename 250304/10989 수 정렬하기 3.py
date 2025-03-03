from sys import stdin
stdin = open('input.txt')
n = stdin.readline
r = [0] * 10001
for _ in range(int(n())): r[int(n())] += 1
for i in range(1, 10001):
    if r[i] > 0 :
        for _ in range(r[i]): print(i)