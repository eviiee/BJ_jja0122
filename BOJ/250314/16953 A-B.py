from collections import deque
a, b = map(int, input().split())
q = deque([(a,1)])

while q:
    x, c = q.popleft()
    for y in [2*x, x*10 + 1]:
        if y > b : continue
        if y == b :
            print(c + 1)
            break
        q.append((y, c+1))
    else: continue
    break
else:
    print(-1)