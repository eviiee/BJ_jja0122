N, r, c = map(int, input().split())

def search(x : int, y : int, n : int):
    if n == 0 : return 0
    mid = 2**(n-1)
    base = (2**(n-1))**2
    if x < mid:
        if y < mid : return search(x, y, n-1)
        else : return base + search(x, y - mid, n-1)
    else:
        if y < mid : return 2*base + search(x - mid, y, n-1)
        else : return 3 * base + search(x - mid, y - mid, n-1)

print(search(r, c, N))