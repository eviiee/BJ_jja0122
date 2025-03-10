from sys import stdin
stdin = open('input.txt')

N, M = map(int, stdin.readline().split(' '))
L1 = set([stdin.readline().rstrip() for _ in range(N)])
L2 = set([stdin.readline().rstrip() for _ in range(M)])
R = L1 & L2

print(len(R))
print(*sorted(list(R)),sep='\n')