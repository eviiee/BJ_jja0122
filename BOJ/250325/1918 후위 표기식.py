operators = []
R = []

for i, c in enumerate(input()):
    if c in '*/':
        if operators and operators[-1] in '*/' : R.append(operators.pop())
        operators.append(c)
    elif c == '(' :
        operators.append(c)
    elif c == ')':
        while operators[-1] != '(': R.append(operators.pop())
        operators.pop()
    elif c in '-+':
        while operators and operators[-1] != '(' : R.append(operators.pop())
        operators.append(c)
    else : R.append(c)
while operators: R.append(operators.pop())


print(''.join(R))