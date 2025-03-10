# def main():
#     N = int(input())
#     M = int(input())
#     S = input()
#     s = 'IO' * N + 'I'
#     l = 2 * N + 1
#     r = 0
#     for i in range(M - l + 1):
#         if S[i] != 'I' : continue
#         if S[i:i+l] == s : r += 1
#     print(r)

def main():
    N = int(input())
    M = int(input())
    S = input().split('O')

    r = 0
    n = 0
    for s in S:
        if s == 'I' :
            n += 1
            continue
        if s : n += 1
        if n > N: r += n - N
        n = int(s != '')
    if n > N : r += n - N
    print(r)


main()