N = int(input())

def draw(n : int):
    if n == 3 : return ['  *  ', ' * * ', '*****']
    sub = draw(n//2)
    spacer = ' ' * (n//2)
    r = []
    for s in sub:
        r.append(spacer + s + spacer)
    for s in sub:
        r.append(s + ' ' + s)
    return r

print(*draw(N), sep='\n')