from sys import stdin
N, M = map(int, stdin.readline().split(' '))
nums = [0] + list(map(int, stdin.readline().split(' ')))
for x in range(1, N+1):
    nums[x] += nums[x-1]
for _ in range(M):
    i, j = map(int, stdin.readline().split(' '))
    print(nums[j] - nums[i-1])
