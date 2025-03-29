from sys import stdin

stdin = open('input.txt')

for line in stdin.readlines()[:-1:]:
    r = 0
    for c in line.lower():
        if c.lower() in 'aeiou': r+=1
    print(r)