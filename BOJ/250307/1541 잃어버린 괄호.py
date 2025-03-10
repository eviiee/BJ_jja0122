f = [sum(int(x) for x in y.split('+')) for y in input().split('-')]
r = 2*f[0]
for i in f: r-=i
print(r)