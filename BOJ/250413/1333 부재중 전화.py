N, L, D = map(int, input().split())

r = 0
s = set()

for i in range(1, N):
    for x in range(5) : s.add(i * L + (i - 1) * 5 + x)

r = 0
while r < N * L + (N - 1) * 5:
    if r in s : break
    r += D

print(r)