n = input().zfill(2)
t = n
r = 0
while 1:
    r += 1
    n = n[-1] + str(sum(map(int, n)))[-1]
    if n == t : break
print(r)