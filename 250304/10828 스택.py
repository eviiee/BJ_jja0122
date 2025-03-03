from sys import stdin

stdin = open('input.txt')

def main():

    s = []
    commands = stdin.read().splitlines()[1::]

    for command in commands:
        l = command.split(' ')
        c = l[0]
        if c == 'push' : s.append(int(l[1]))
        elif c == 'pop' : print(s.pop() if len(s) > 0 else -1)
        elif c == 'size' : print(len(s))
        elif c == 'empty' : print(int(len(s) == 0))
        elif c == 'top' : print(s[-1] if len(s) > 0 else -1)

if __name__ == '__main__' :
    main()