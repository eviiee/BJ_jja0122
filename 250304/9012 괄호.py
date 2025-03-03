from sys import stdin

def main():
    cases = stdin.read().splitlines()[1::]
    for case in cases:
        n = 0
        for c in case:
            if c == '(': n+=1
            elif n == 0:
                print('NO')
                break
            else: n -= 1
        else: print('YES') if n ==0 else print('NO')

if __name__ == '__main__':
    main()