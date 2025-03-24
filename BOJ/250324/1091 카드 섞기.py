N = int(input())
P, S = list(map(int, input().split())), {}
for i, j in enumerate(map(int, input().split())): S[j] = i
cards = [i for i in range(N)]
history = set()

r = 0
while True:
    h = [0] * N
    for i, card in enumerate(cards): h[card] = i
    h = tuple(h)
    if h in history :
        r = -1
        break
    else : history.add(h)
    
    for i in range(N):
        if i%3 != P[cards[i]]: break
    else: break
    cards = [cards[S[i]] for i in range(N)]
    r += 1

print(r)