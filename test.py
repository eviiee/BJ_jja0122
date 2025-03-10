import heapq



occupied = 0
occupied_until = [0] * 5

for st, ed, _ in [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]:
    if occupied < 3:
        heapq.heap()