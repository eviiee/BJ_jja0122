from sys import stdin
stdin = open('input.txt')

def main():
    N = []
    n = int(stdin.readline())
    l = 0
    r = ''
    for _ in range(n):
        x = int(stdin.readline())
        if x > l :
            N += [i for i in range(l+1, x)]
            r += '+' * (x - l) + '-'
            l = x
        else:
            if not N or N[-1] != x :
                print('NO')
                return
            else :
                r += '-'
                N.pop()
    print(*r, sep='\n')

if __name__ == '__main__' : main()