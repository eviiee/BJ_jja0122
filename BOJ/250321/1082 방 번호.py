N = int(input())
price = list(map(int, input().split()))
M = int(input())

# def needupdate(i, j):
#     count = D[i-price[j]][-1]
#     current = D[i][-1]
#     if j == count == 0 : return False
#     if count + 1 < current : return False
#     if count + 1 == current :
#         for x in range(N-1, -1, -1):
#             t = 1 if x == j else 0
#             if D[i][x] == D[i-price[j]][x] + t == 0 : continue
#             if D[i][x] > D[i-price[j]][x] + t : return False
#             break
#     return True

# D = [[0]*(N+1) for _ in range(M + 1)]
# for i in range(1, M+1):
#     for j in range(N):
#         if i - price[j] < 0 : continue
#         if not needupdate(i, j) : continue
#         for k in range(N+1): D[i][k] = D[i-price[j]][k]
#         D[i][j] += 1
#         D[i][-1] += 1
# R = []
# for i in range(N):
#     for j in range(D[-1][i]): R.append(i)
# if not R : R.append(0)
# R.sort(reverse=True)
# print(*R, sep='')

D = [0] * (M+1)

for i in range(N-1, -1, -1):
    for j in range(price[i], M+1):
        D[j] = max(D[j], 10*D[j-price[i]] + i)

print(D[-1])