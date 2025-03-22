
N, K = map(int, input().split())

def solve(n, k):
    if k <= n : return n - k
    from collections import deque

    q = deque([(n, 0)])
    V = [False] * (k + 3)
    V[n] = True
    while q:
        x, c = q.popleft()
        if x == k : return c
        for y in (x - 1, x + 1, x * 2):
            if not 0<y<len(V) or V[y]: continue
            if y == x * 2 : q.appendleft((y, c))
            else : q.append((y, c+1))
            V[y] = True

print(solve(N, K))