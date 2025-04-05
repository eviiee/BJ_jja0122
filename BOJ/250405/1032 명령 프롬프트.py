N = int(input())
C = [input() for _ in range(N)]

R = ''
for i in range(len(C[0])):
    c = C[0][i]
    for j in range(N):
        if c != C[j][i] :
            R += '?'
            break
    else:
        R += c
    
print(R)