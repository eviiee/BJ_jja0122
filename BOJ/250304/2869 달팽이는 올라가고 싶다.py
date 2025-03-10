from math import ceil
A, B, V = map(int, input().split(' '))
if V == A : print(1)
else: print(1 + ceil((V - A) / (A - B)))