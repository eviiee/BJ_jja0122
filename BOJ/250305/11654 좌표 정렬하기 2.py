from sys import stdin
stdin = open('input.txt')

def main():
    C = [tuple(map(int, c.split(' '))) for c in stdin.read().splitlines()[1::]]
    C.sort(key=lambda x: (x[1],x[0]))
    for c in C:
        print(*c)

if __name__ == '__main__' : main()