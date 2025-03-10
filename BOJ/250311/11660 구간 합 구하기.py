from sys import stdin
stdin = open('input.txt')

N, M = map(int,stdin.readline().split())
nums = [list(map(int, stdin.readline().split())) for _ in range(N)]
S = [[0] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        S[i][j] = S[i-1][j] + S[i][j-1] + nums[i-1][j-1] - S[i-1][j-1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(S[x2][y2] + S[x1-1][y1-1] - S[x1-1][y2] - S[x2][y1-1])