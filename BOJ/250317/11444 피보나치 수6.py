n = int(input())
mod = 1000000007
m = {0 : 0, 1 : 1, 2 : 1, 3 : 2, 4 : 3, 5 : 5}

def solve(n : int):
    if n in m : return m[n]
    r = (solve(n//2 + 1)**2 + solve(n//2)**2 if n&1 else solve(n//2) * (solve(n//2) + 2 * solve(n//2 - 1))) % mod
    m[n] = r
    return r

print(solve(n))