#https://school.programmers.co.kr/learn/courses/30/lessons/389481

def solution(n, bans):
    bans.sort(key=lambda x: (len(x),x))
    nums = [toNum(s) for s in bans]
    for num in nums:
        if n >= num : n += 1
        else : break
        
    return toStr(n)

def toNum(s : str) -> int:
    base = ord('a')
    r = 0
    for i, c in enumerate(s[::-1]):
        n = ord(c) - base + 1
        r += 26 ** i * n
    return r

def toStr(num: int) -> str:
    result = []
    base = ord('a')
    while num > 0:
        num -= 1
        result.append(chr(base + (num % 26)))
        num //= 26
    
    return ''.join(result[::-1])
