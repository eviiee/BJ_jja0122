from sys import stdin
stdin = open('input.txt')

def main():
    N = []
    for _ in range(int(stdin.readline())):
        n = int(stdin.readline())
        if n == 0 : N.pop()
        else: N.append(n)

    print(sum(N))

if __name__ == '__main__' : main()