from bisect import bisect_left

N = int(input())
nums = list(map(int, input().split(' ')))
sNums = sorted(set(nums))

for i, num in enumerate(nums): nums[i] = bisect_left(sNums, num)
print(*nums)