from itertools import permutations
N, M = map(int,input().split())
combs = list(set(permutations(map(int, input().split()), M)))
combs.sort()
for comb in combs:print(*comb)