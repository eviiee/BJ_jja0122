s1, s2 = input(), input()
n, m = len(s1), len(s2)

D = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        D[i][j] = D[i-1][j-1] + 1 if s1[i-1] == s2[j-1] else max(D[i-1][j], D[i][j-1])

print(D[-1][-1])