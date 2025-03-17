N = int(input())
house = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
D = [[[0] * (N+1) for _ in range(N+1)] for t in range(3)]
D[0][1][2] = 1
for i in range(1, N+1):
    for j in range(2, N+1):
        if i == 1 and j == 2 : continue
        if house[i][j] == 1 : continue
        D[0][i][j] = D[0][i][j-1] + D[2][i][j-1]
        D[1][i][j] = D[1][i-1][j] + D[2][i-1][j]
        if house[i-1][j] == 1 or house[i][j-1] == 1 : continue
        D[2][i][j] = D[0][i-1][j-1] + D[1][i-1][j-1] + D[2][i-1][j-1]

print(D[0][-1][-1] + D[1][-1][-1] + D[2][-1][-1])