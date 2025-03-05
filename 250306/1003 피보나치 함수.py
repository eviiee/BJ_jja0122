from sys import stdin
D = [()] * 41
D[0],D[1] = (1,0),(0,1)
for i in range(2, 41): D[i] = (D[i-1][0] + D[i-2][0], D[i-1][1] + D[i-2][1])
for _ in range(int(stdin.readline())): print(*D[int(stdin.readline())])