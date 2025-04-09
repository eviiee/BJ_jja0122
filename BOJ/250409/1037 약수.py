N = int(input())
nums = list(map(int, input().split()))
from math import lcm
x = lcm(*nums)
if x == max(nums) : x *= min(nums)
print(x)