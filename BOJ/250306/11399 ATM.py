N = int(input())
P = list(map(int, input().split(' ')))
P.sort()

r = 0
s = 0

for p in P:
    s += p
    r += s

print(r)