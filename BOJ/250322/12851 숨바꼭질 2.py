N, K = map(int, input().split())

def solve(n, k):

    if k <= n : return (n - k, 1)
    from collections import deque

    q = deque([n])
    V = [[0, 0] for _ in range(k + 2)]
    V[n] = [1, 1]

    while q:
        x = q.popleft()
        c = V[x][0]

        for y in (x-1, x+1, x*2):

            nc = c + 1

            if V[k][0] and V[k][0] < nc : continue
            if not 0<y<len(V): continue

            if V[y][0]:
                if nc > V[y][0] : continue
            else:
                V[y][0] = nc
                q.append(y)

            V[y][1] += V[x][1]

    return (V[k][0] - 1, V[k][1])

print(*solve(N, K), sep='\n')