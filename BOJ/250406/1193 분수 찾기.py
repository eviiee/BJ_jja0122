X = int(input())

t, i = 0, 1
while t + i < X :
    t += i
    i += 1

a = X - t
b = i + 1 - X + t

if i&1 : a, b = b, a

print(f'{a}/{b}')