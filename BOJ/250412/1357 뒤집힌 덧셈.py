rev = lambda x : ''.join(reversed(x))
a, b = input().split()
print(int(rev(str(int(rev(a)) + int(rev(b))))))