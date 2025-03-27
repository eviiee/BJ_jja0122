N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

R = [[[] for _ in range(M+1)] for _ in range(N+1)]

def l(arr1, arr2):
    if arr1 == arr2 : return arr1
    for i in range(min(len(arr1), len(arr2))):
        if arr1[i] > arr2[i] : return arr1
        if arr1[i] < arr2[i] : return arr2
    if len(arr1) > len(arr2) : return arr1
    else : return arr2

for r in range(1, N+1):
    for c in range(1, M+1):
        if A[r-1] == B[c-1] :
            temp = R[r-1][c-1][::]
            for i in range(len(temp)-1, -1, -1):
                if temp[i] < A[r-1]: temp.pop()
                else:  break
            temp.append(A[r-1])
            R[r][c] = temp
        else : R[r][c] = l(R[r-1][c], R[r][c-1])

print(len(R[-1][-1]))
print(*R[-1][-1])