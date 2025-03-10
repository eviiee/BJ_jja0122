from collections import deque
from sys import stdin
stdin = open('input.txt')

def main():
    try:
        commands = stdin.readline().rstrip()
        n = int(stdin.readline())
        l = []
        if n == 0: stdin.readline()
        else : l = stdin.readline().rstrip()[1:-1].split(',')
        nums = deque(l)
        reverse = False
        for command in commands:
            if command == 'R': reverse = not reverse
            else : nums.pop() if reverse else nums.popleft()
        if reverse : nums.reverse()
        print(f'[{",".join(nums)}]')
    except:
        print('error')

for _ in range(int(stdin.readline())): main()