from sys import stdin
stdin = open('input.txt')
_ = stdin.readline()
meetings = {}

for m in stdin.readlines():
    st, ed = map(int, m.split())
    if not ed in meetings : meetings[ed] = [-1, 0]
    if st == ed : meetings[ed][1] += 1
    else : meetings[ed][0] = max(meetings[ed][0], st)  

r = 0
last = 0
for time in sorted(meetings.keys()):
    info = meetings[time]
    if last <= info[0] :
        r += 1
        last = time
    if info[1] > 0 :
        r += info[1]
        last = time

print(r)