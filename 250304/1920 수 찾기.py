_ = input()
A = set(map(int, input().split(' ')))
_ = input()
M = map(int, input().split(' '))

for m in M: print(int(m in A))