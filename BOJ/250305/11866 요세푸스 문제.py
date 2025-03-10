from collections import deque
N, K = map(int, input().split(' '))
q = deque([str(i) for i in range(1, N+1)])
r = []
while q:
    q.rotate(-(K-1))
    r.append(q.popleft())
print(f'<{", ".join(r)}>')