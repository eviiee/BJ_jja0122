count = [0, 0]

def divide(p : list):
    global count
    color = sum([sum(row) for row in p])
    if color == 0:
        count[0] += 1
        return
    x, y = len(p), len(p[0])
    if color == x * y:
        count[1] += 1
        return
    divide([row[:y//2] for row in p[:x//2]])
    divide([row[:y//2] for row in p[x//2:x]])
    divide([row[y//2:y] for row in p[:x//2]])
    divide([row[y//2:y] for row in p[x//2:x]])


P = [list(map(int, input().split(' '))) for _ in range(int(input()))]
divide(P)
print(*count, sep='\n')