from sys import stdin
stdin = open('input.txt')

def main():
    lines = stdin.read().splitlines()[:-1:]
    for line in lines: validate(line)

def validate(line : str):
    
    B = []

    for c in line :
        if c == '(' : B.append(True)
        elif c == '[' : B.append(False)
        elif (c == ')' or c == ']') and not B : break
        elif c == ')' and not B.pop() : break
        elif c == ']' and B.pop() : break
    else:
        print('yes') if len(B) == 0 else print('no')
        return
    print('no')

if __name__ == '__main__' : main()