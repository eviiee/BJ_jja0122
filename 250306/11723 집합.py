from sys import stdin
stdin = open('input.txt')

def main():
    r = set()
    for _ in range(int(stdin.readline())):
        C = stdin.readline().rstrip().split(' ')
        c = C[0]
        if c == 'empty': r.clear()
        elif c == 'all': r = {i for i in range(1, 21)}
        if c == 'empty' or c == 'all' : continue
        v = int(C[1])
        if c == 'add':  r.add(v)
        elif c == 'remove': r.discard(v)
        elif c == 'check': print(int(v in r))
        elif c == 'toggle': r.remove(v) if v in r else r.add(v)
        
if __name__ == '__main__' : main()
