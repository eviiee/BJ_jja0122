from sys import stdin
N = int(stdin.readline())
S = [0] * N
for i in range(N):
    nums = list(map(int, stdin.readline().split()))
    for j in range(i, -1, -1):
        m = 0
        if j == 0 : m = S[0]
        else : m = max(S[j],S[j-1])
        S[j] = m + nums[j]

print(max(S))