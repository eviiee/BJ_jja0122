from sys import stdin
from collections import deque

def main():
    for _ in range(int(stdin.readline())):

        N, M = map(int, stdin.readline().split(' '))
        D = deque([(idx, x) for idx, x in enumerate(map(int, stdin.readline().split(' ')))])
        
        count = 0
    
        while (1) :
            d = D.popleft()
            if not D or d[1] >= max([x[1] for x in D]):
                count += 1
                if d[0] == M : break
            else: D.append(d)

        print(count)
    

if __name__ == '__main__' : main()