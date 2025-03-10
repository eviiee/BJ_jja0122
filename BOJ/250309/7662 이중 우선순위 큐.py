import heapq
from sys import stdin
from collections import defaultdict as dd
stdin = open('input.txt')

for t in range(int(stdin.readline())):

    maxHeap = []
    minHeap = []
    counter = dd(int)

    for _ in range(int(stdin.readline())):
        command, num = stdin.readline().split()
        if command == 'I':
            n = int(num)
            heapq.heappush(minHeap, n)
            heapq.heappush(maxHeap, -n)
            counter[n] += 1
            continue

        while maxHeap and minHeap:
            n = heapq.heappop(minHeap) if num == '-1' else heapq.heappop(maxHeap) * -1
            if counter[n] > 0:
                counter[n] -= 1
                break
        
    
    if sum(counter.values()) == 0 :
        print('EMPTY')
        continue

    r = []

    while True:
        maxVal = heapq.heappop(maxHeap) * -1
        if counter[maxVal] > 0 :
            r.append(maxVal)
            break

    while True:
        minVal = heapq.heappop(minHeap)
        if counter[minVal] > 0 :
            r.append(minVal)
            break
    
    print(*r)
            