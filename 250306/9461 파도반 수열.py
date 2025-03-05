D = [1,1,1,2,2]
for i in range(5, 101): D.append(D[i-1] + D[i-5])
for _ in range(int(input())):
    print(D[int(input()) - 1])