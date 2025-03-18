s1 = input()
s2 = list(input())
L = len(s2)
ans = []

def check():
    if len(ans) < L : return
    if ans[-L:] == s2:
        for _ in range(L) : ans.pop()
        check()

for c in s1:
    ans.append(c)
    check()

print(''.join(ans) if ans else 'FRULA')
