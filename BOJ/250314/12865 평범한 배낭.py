from sys import stdin

N, K = map(int, stdin.readline().split())
objects = [tuple(map(int, stdin.readline().split())) for _ in range(N)]
D = [0] * (K + 1)

for w, v in objects:
    for i in range(K, w-1, -1):
        D[i] = max(D[i - w] + v, D[i])

print(D[-1])
