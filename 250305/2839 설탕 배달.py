def main():

    n = int(input())
    D = [-1] * 5001

    D[3] = 1
    D[5] = 1

    if n <= 5 :
        print(D[n])
        return
    
    for i in range(6, n+1):
        if D[i-3] != -1: D[i] = D[i-3] + 1
        if D[i-5] != -1: D[i] = min(D[i], D[i-5]+1) if D[i] != -1 else D[i-5] + 1
        
    print(D[n])

if __name__ == '__main__' : main()