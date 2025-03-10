from collections import defaultdict as d

_ = input()
fruits = list(map(int, input().split()))

st, ed, r = 0,0,0
counter = d(int)
count = 0

while len(fruits) > ed:

    if counter[fruits[ed]] == 0 : count+=1
    counter[fruits[ed]] += 1

    while count > 2 :
        counter[fruits[st]] -= 1
        if counter[fruits[st]] == 0 : count -= 1
        st += 1
    
    r = max(r, ed - st + 1)
    ed += 1
    
print(r)