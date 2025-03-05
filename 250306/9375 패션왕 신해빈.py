from sys import stdin
for _ in range(int(stdin.readline())):
    C = {}
    for _ in range(int(stdin.readline())):
        t = stdin.readline().split(' ')[1]
        if not t in C : C[t] = 0
        C[t] += 1
        
    r = 1
    for i in C.values(): r *= i + 1

    print(r - 1)