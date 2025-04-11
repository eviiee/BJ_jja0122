from sys import stdin

c = 0
while 1:
    N = int(stdin.readline())
    if not N : break
    c += 1
    names = [stdin.readline().rstrip() for _ in range(N)]
    r = set()
    for _ in range(2*N-1) :
        n = int(stdin.readline().split()[0])
        if n in r: r.remove(n)
        else : r.add(n)
    print(c, names[r.pop() - 1])