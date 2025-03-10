D = [0] * 1000
D[0], D[1] = 1, 3
for i in range(2, 1000): D[i] = (D[i-1] + 2*D[i-2])%10007
print(D[int(input())-1])