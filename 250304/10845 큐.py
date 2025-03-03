from sys import stdin
from collections import deque

# stdin = open('input.txt')

def main():

    q = deque([])
    commands = stdin.read().splitlines()[1::]

    def pop():
        if not q: print(-1)
        else:
            print(q[0])
            q.popleft()

    for command in commands:
        l = command.split(' ')
        c = l[0]
        if c == 'push' : q.append(int(l[1]))
        elif c == 'pop' : pop()
        elif c == 'size' : print(len(q))
        elif c == 'empty' : print(int(not bool(q)))
        elif c == 'front' : print(q[0] if q else -1)
        elif c == 'back' : print(q[-1] if q else -1)

if __name__ == '__main__' :
    main()