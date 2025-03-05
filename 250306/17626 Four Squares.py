

# n = int(input())

# D = [i for i in range(n+1)]

# for i in range(2, n+1):
#     for j in range(1, int(i**0.5) + 1):
#         D[i] = min(D[i], D[i - j**2] + 1)


# print(D[n])



def solve():
    
    n = int(input())
    sqr = n**0.5

    if sqr.is_integer(): return 1
    for i in range(int(sqr),0,-1):
        if ((n - i**2)**0.5).is_integer(): return 2
    for i in range(int(sqr),0,-1):
        for j in range(int((n - i**2)**0.5),0,-1):
            if ((n - i**2 - j**2)**0.5).is_integer() : return 3
    return 4

print(solve())