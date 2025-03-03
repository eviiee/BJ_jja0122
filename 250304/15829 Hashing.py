L = int(input())
S = input()

hash = 0
for i in range(L):
    c = S[i]
    hash += (ord(c) - ord('a') + 1) * ( 31 ** i )

print(hash % 1234567891)