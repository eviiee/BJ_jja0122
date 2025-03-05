D = [0] * 10
D[0],D[1],D[2] = 1, 2, 4
for i in range(3, 10):
    D[i] = D[i-3] + D[i-2] + D[i-1]

for _ in range(int(input())):
    print(D[int(input()) - 1])