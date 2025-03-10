from queue import SimpleQueue

c = SimpleQueue()

for i in range(1, int(input()) + 1): c.put(i)

while c.qsize() > 1:
    c.get()
    c.put(c.get())

print(c.get())