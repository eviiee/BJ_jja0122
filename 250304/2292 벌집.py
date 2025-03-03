n = int(input())
s = 1
i = 0
while (1):
    s += i * 6
    if s >= n:
        print(i + 1)
        break
    i += 1