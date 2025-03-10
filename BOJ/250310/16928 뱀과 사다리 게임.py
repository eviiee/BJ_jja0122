from sys import stdin
from collections import deque
stdin = open('input.txt')

def main():
    N, M = map(int, stdin.readline().split())
    A = {}
    V = [0] * 101

    for l in stdin.readlines():
        a, b = map(int, l.split())
        A[a] = b
    
    q = deque([1])
    while (1):
        x = q.popleft()
        for dx in range(1, 7):
            nx = x+dx
            if V[nx] or nx > 100 : continue
            if nx in A and not V[nx]:
                V[nx] = V[x] + 1
                if V[A[nx]]: continue
                nx = A[nx]
            V[nx] = V[x] + 1
            if nx == 100 :
                print(V[100])
                return
            q.append(nx)

if __name__ == '__main__' : main()