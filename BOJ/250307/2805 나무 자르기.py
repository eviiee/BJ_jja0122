from collections import Counter
N, M = map(int, input().split(' '))
trees = list(map(int, input().split(' ')))
trees.sort(reverse=True)

lo = 0
hi = trees[0]
counter = Counter(trees)

while lo < hi:
    md = (lo + hi) // 2 + 1
    r = 0
    for tree in counter.keys():
        if tree - md <= 0 : break
        r += counter[tree] * (tree - md)
    if M > r : hi = md - 1
    else : lo = md

print(lo)