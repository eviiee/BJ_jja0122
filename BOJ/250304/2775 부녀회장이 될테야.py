from sys import stdin

def main():
    for _ in range(int(stdin.readline())):
        k = int(stdin.readline())
        n = int(stdin.readline())

        r = [i + 1 for i in range(n)]
        for y in range(k):
            for x in range(n-1, -1, -1):
                r[x] = sum(r[:x+1])
        print(r[-1])

if __name__ == '__main__' : main()