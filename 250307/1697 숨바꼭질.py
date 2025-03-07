from collections import deque

N, K = map(int, input().split(' '))
V = [False] * 100001
q = deque([(N,0)])

while (1):
    n, c = q.popleft()

    if n == K :
        print(c)
        break
    
    for dn in [n-1, n+1, n*2]:
        if 0<=dn<=100000 and not V[dn]:
            V[dn] = True
            q.append((dn, c+1))