from sys import stdin

N = int(stdin.readline())
s = [list(map(int, stdin.readline().split())) for _ in range(N)]
R = [[False] * N for _ in range(N)]

for j in range(5):
    for i in range(N):
        for k in range(i + 1, N):
            if s[i][j] == s[k][j] :
                R[i][k] = True
                R[k][i] = True

R = [sum(row) for row in R]
r = 0
for i in range(N):
    if R[i] > R[r] : r = i

print(r + 1)