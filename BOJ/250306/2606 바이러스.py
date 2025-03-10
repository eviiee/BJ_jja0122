from sys import stdin
from collections import deque

def main():

    N = int(stdin.readline())
    G = {i : [] for i in range(1, N+1)}
    
    for _ in range(int(stdin.readline())):
        a, b = map(int, stdin.readline().split(' '))
        G[a] += [b]
        G[b] += [a]
        
    q = deque([1])
    V = {1}

    while q:
        i = q.popleft()
        for j in G[i]:
            if j in V: continue
            V.add(j)
            q.append(j)
    
    print(len(V) - 1)


if __name__ == '__main__' : main()