from sys import stdin
stdin = open('input.txt')

N, M = map(int, stdin.readline().split())
K = set(map(int, stdin.readline().split()[1::]))
parties = [set(map(int, line.split()[1::])) for line in stdin.readlines()]
R = {i for i in range(len(parties))}

while 1:
    s = True
    for i in list(R):
        party = parties[i]
        if not K&party : continue
        s = False
        K.update(party)
        R.remove(i)
    if s : break

print(len(R))