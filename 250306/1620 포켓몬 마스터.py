from sys import stdin
stdin = open('input.txt')

def main():
    N, M = map(int, stdin.readline().split(' '))
    P1 = [stdin.readline().rstrip() for _ in range(N)]
    P2 = {val : idx + 1 for idx, val in enumerate(P1)}

    for _ in range(M):
        l = stdin.readline()
        try: print(P1[int(l) - 1])
        except: print(P2[l.rstrip()])

if __name__ == '__main__' : main()