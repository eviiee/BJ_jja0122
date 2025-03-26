N = int(input())
occ1 = [False] * N
occ2 = [False] * (2*N-1)
occ3 = [False] * (2*N-1)

r = 0

def solve(i : int):
    global r
    if i == N :
        r+=1
        return
    for j in range(N):
        if i == 0:
            if N&1 :
                if j == N//2 : r*=2
                elif j > N//2 : return
            elif j == N//2 :
                r*=2
                return
        if occ1[j] or occ2[i + j] or occ3[N + i - j - 1]: continue
        occ1[j] = True
        occ2[i + j] = True
        occ3[N + i - j - 1] = True
        solve(i + 1)
        occ1[j] = False
        occ2[i + j] = False
        occ3[N + i - j - 1] = False

solve(0)
print(r)