from itertools import permutations

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

for n in permutations(nums, M): print(*n)