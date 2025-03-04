from sys import stdin

def main():
    K, N = map(int, stdin.readline().split(' '))
    L = [int(stdin.readline()) for _ in range(K)]

    L.sort()

    lo = 1
    hi = L[-1]

    while lo < hi :
        r = (lo + hi) // 2 + 1
        n = sum([l // r for l in L])
        if n < N : hi = r - 1
        else : lo = r

    print(hi)

if __name__ == '__main__' : main()