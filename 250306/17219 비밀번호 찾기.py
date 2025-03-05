from sys import stdin
stdin = open('input.txt')

N, M = map(int, stdin.readline().split(' '))
P = {}
for _ in range(N):
    domain, password = stdin.readline().rstrip().split(' ')
    P[domain] = password
for _ in range(M):
    print(P[stdin.readline().rstrip()])