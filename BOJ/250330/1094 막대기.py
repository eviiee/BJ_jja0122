X = int(input())

s = 64
l = s
r = 1

while l > X:
    s //= 2
    if l - s >= X : l -= s
    else : r += 1

print(r)
