N = int(input())
nums = list(map(int, input().split()))
D = [1] * N

for i, num in enumerate(nums) :
    for j in range(i):
        if nums[j] < num : D[i] = max(D[i], D[j] + 1)
print(max(D))
