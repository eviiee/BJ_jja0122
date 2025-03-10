from sys import stdin

def main():
    _ = stdin.readline()
    N = map(int, stdin.readline().split(' '))
    _ = stdin.readline()
    M = map(int, stdin.readline().split(' '))

    count = {}

    for n in N:
        if n in count: count[n] += 1
        else: count[n] = 1

    print(*[count[m] if m in count else 0 for m in M])

main()