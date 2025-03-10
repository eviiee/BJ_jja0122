def main():
    
    P = []
    for _ in range(int(input())):
        P.append(tuple(map(int, input().split(' '))))

    s = []
    for i in range(len(P)):
        r = 1
        for j in range(len(P)):
            if i == j : continue
            if P[i][0] < P[j][0] and P[i][1] < P[j][1]: r+=1
        s.append(r)
    
    print(*s)

if __name__ == '__main__' : main()