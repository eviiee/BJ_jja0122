def main():
    M, N = map(int, input().split(' '))

    D = [True] * (N + 1)
    D[1] = False
    
    for i in range(2, int(N ** 0.5) + 1):
        if D[i] :
            for j in range(i * i, N + 1, i):
                D[j] = False
    
    for i in range(M, N+1):
        if D[i] : print(i)


if __name__ == '__main__' : main()