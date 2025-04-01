from sys import stdout
from random import randint
# print = stdout.write
output = open('input.txt', 'w')

def tc2467():
    N = randint(2, 20)
    print(N, file=output)
    r = set()

    while len(r) < N:
        n = 0
        while n in r or n == 0 :
            n = randint(-10**9, 10**9)
        r.add(n)
    
    r = list(r)
    r.sort()
    print(*r, file=output)

tc2467()