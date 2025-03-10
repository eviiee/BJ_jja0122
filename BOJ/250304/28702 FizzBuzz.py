N = [input() for _ in range(3)]
i = 0
while (1):
    if not N[i] in {'Fizz', 'Buzz', 'FizzBuzz'}: break
    i += 1
n = int(N[i]) + 3 - i
r = ''
if n % 3 == 0 : r += 'Fizz'
if n % 5 == 0 : r += 'Buzz'
if len(r) == 0 : r = str(n)
print(r)