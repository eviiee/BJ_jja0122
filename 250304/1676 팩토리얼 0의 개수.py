from math import factorial
n = int(input())
x = factorial(n)
r = 0
for c in str(x)[::-1]:
    if c != '0': break
    r += 1
print(r)