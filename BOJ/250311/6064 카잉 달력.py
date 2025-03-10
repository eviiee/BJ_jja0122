from sys import stdin
from math import lcm
for _ in range(int(stdin.readline())):

    M, N, x, y = map(int, stdin.readline().split())
    
    l = lcm(M, N)
    k = x
    while k <= l:
        if k%N == y%N :
            print(k)
            break
        k += M
    else : print(-1)
