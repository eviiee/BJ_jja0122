from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    scores = [list(map(int, stdin.readline().split())) for _ in range(2)]
    s1, s2, s3 = scores[0][0], scores[1][0], 0

    for i in range(1, n): s1, s2, s3 = max(s2, s3) + scores[0][i], max(s1, s3) + scores[1][i], max(s1, s2, s3)

    print(max(s1, s2, s3))