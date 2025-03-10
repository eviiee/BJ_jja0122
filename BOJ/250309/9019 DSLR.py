from collections import deque
from sys import stdin
stdin = open('input.txt')

def bfs():
    a, b = map(int, stdin.readline().split())
    V = [[] for _ in range(10001)]
    q = deque([a])
    ops = [D, S, L, R]

    while q:
        x = q.popleft()
        for op in ops:
            y = op(x)
            if y == a or V[y] : continue
            V[y] = V[x].copy()
            V[y].append(op.__name__)
            if y == b:
                print(''.join(V[b]))
                return
            q.append(y)

def D(x : int): return (2 * x) % 10000
def S(x : int): return (9999 + x) % 10000
def L(x : int): return x%1000 * 10 + x//1000
def R(x : int): return x//10 + x%10*1000

for _ in range(int(stdin.readline())): bfs()