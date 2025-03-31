N = int(input())
sq = list(map(int, input().split()))

R1 = [1] * N
R2 = [1] * N

def solve(arr : list):
    global sq
    for i, n in enumerate(sq):
        for j in range(i):
            if n > sq[j] : arr[i] = max(arr[i], arr[j] + 1)
    
solve(R1)
sq.reverse()
solve(R2)
R2.reverse()

r = max(sum(x) for x in zip(R1, R2))
print(r-1)