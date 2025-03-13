from itertools import combinations_with_replacement
N,M = map(int,input().split())
nums = sorted(map(int,input().split()))
for comb in sorted(set(combinations_with_replacement(nums, M))): print(*comb)