# def s(a : int, b: int):
#     if b == 1: return a % c
#     x = s(a, b//2)
#     if b&1 : return (a * x**2) % c
#     return (x**2) % c

# a, b, c = map(int, input().split())
# print(s(a, b))

print(pow(*map(int, input().split())))