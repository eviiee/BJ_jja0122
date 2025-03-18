from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)
stdin = open('input.txt')
pret = list(map(int, stdin.readlines()))
def traverse(st : int, ed: int):
    if st > ed: return
    if st < ed:
        i = st + 1
        while i <= ed:
            if pret[i] > pret[st] : break
            i+=1
        traverse(st+1, i-1)
        traverse(i, ed)
    print(pret[st])
    return
traverse(0, len(pret)-1)