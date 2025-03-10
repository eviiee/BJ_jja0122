from sys import stdin
stdin = open('input.txt')

def round(n : float):
    if n - int(n) >= 0.5 :
        return int(n) + 1
    else :
        return int(n)

def main():
    n = int(stdin.readline())
    if n == 0 :
        print(0)
        return
    r = round(n * 0.15)
    s = list(map(int, stdin.readlines()))
    s.sort()
    s = s[r:n-r:]
    print(round(sum(s) / len(s)))

if __name__ == '__main__' : main()