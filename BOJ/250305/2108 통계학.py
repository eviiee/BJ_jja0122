from sys import stdin
from collections import Counter

stdin = open('input.txt')

def main():
    N = int(stdin.readline())
    nums = list(map(int, stdin.read().splitlines()))
    nums.sort()
    counter = Counter(nums).most_common(2)

    mode = counter[0][0]
    if len(counter) > 1 and counter[0][1] == counter[1][1] : mode = counter[1][0]

    print(round(sum(nums) / N))
    print(nums[N // 2])
    print(mode)
    print(nums[-1] - nums[0])

if __name__ == '__main__' : main()