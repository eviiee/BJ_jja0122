from sys import stdin
stdin = open('input.txt')

N, K = map(int, stdin.readline().split(' '))
C = list(map(int, stdin.read().splitlines()))
r = 0
for i in reversed(C):
    r += K // i
    K %= i

print(r)