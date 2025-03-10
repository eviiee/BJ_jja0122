#https://school.programmers.co.kr/learn/courses/30/lessons/214288

import heapq

def solution(k, n, reqs):
    
    meetings = [[] for _ in range(k)]
    for st, ed, k_type in reqs:
        meetings[k_type-1].append((st, ed))
        
    mentors = [1] * k
    current_waiting = [getWaitTime(k_type, 1) for k_type in meetings]
    if k == n : return sum(current_waiting)

    next_waiting = [current_waiting[i] - getWaitTime(meetings[i], 2) for i in range(k)]
    n -= k
    while n :
        k_type = next_waiting.index(max(next_waiting))
        mentors[k_type] += 1
        current_waiting[k_type] -= next_waiting[k_type]
        next_waiting[k_type] = current_waiting[k_type] - getWaitTime(meetings[k_type], mentors[k_type] + 1)
        n -= 1  
    return sum(current_waiting)

def getWaitTime(meetings, n):
    
    occupied_until = [0] * n
    wait_time = 0
    
    for st, length in meetings:
        ed_time = heapq.heappop(occupied_until)
        if ed_time > st :
            wait_time += ed_time - st
            st = ed_time
        heapq.heappush(occupied_until, st + length)
        
    return wait_time