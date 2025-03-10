from sys import stdin
stdin = open('input.txt')

def main():

    N = int(stdin.readline())
    scores = list(map(int, stdin.readlines()))

    if N <= 2: 
        print(sum(scores))
        return
    
    D = [[0,0] for _ in range(N)]
    D[0] = [scores[0],0]
    D[1] = [scores[0]+scores[1],scores[1]]
    D[2] = [scores[1]+scores[2],scores[0]+scores[2]]
    for i in range(3, N):
        D[i][0] = max(D[i-3]) + scores[i-1] + scores[i]
        D[i][1] = max(D[i-2]) + scores[i]

    print(max(D[-1]))

if __name__ == '__main__' : main()