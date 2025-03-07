from collections import Counter
_ = input()
last = 0
fruits = []

for fruit in map(int, input().split(' ')):
    if last != fruit:
        last = fruit
        fruits += [1]
    else:
        fruits[-1] += 1

if len(fruits) == 1 : print(len(fruits))
else:
    r = 0
    for i in range(len(fruits) - 1):
        r = max(r, fruits[i] + fruits[i+1])
    print(r)