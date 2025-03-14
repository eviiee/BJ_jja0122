from sys import stdin

N = int(stdin.readline())

min_r, max_r = [0] * 3, [0] * 3

for i in range(N):

    scores = list(map(int, stdin.readline().split()))

    if i == 0:
        min_r = scores.copy()
        max_r = scores.copy()
        continue
        
    min_r = [
        min(min_r[0], min_r[1]) + scores[0],
        min(min_r) + scores[1],
        min(min_r[1], min_r[2]) + scores[2],
    ]

    max_r = [
        max(max_r[0], max_r[1]) + scores[0],
        max(max_r) + scores[1],
        max(max_r[1], max_r[2]) + scores[2],
    ]


print(*[max(max_r), min(min_r)])