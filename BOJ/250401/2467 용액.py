from sys import stdin
stdin = open('input.txt')

def find():
    N = int(stdin.readline())
    ph = list(map(int, stdin.readline().split()))
    import bisect

    hi = N
    v = abs(ph[0] + ph[-1])
    r = (0, N - 1)

    for a in range(N-1):
        hi = bisect.bisect_right(ph, -ph[a], lo=a+1, hi=hi)
        b = hi
        if b < N and abs(ph[a] + ph[b]) < v :
            v = abs(ph[a] + ph[b])
            r = (a, b)
        if b - 1 > a and abs(ph[a] + ph[b - 1]) < v :
            v = abs(ph[a] + ph[b - 1])
            r = (a, b - 1)
    
    return (ph[r[0]], ph[r[1]])
        

print(*find())

