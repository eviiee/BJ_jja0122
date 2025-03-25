N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

R = []

i, j = 0, 0
while 1:
    arr1, arr2 = A[i:], B[j:]
    c = set(arr1).intersection(set(arr2))
    if not c: break
    gcn = max(c)
    R.append(gcn)
    i, j = A.index(gcn) + 1, B.index(gcn) + 1

print(len(R))
print(*R)