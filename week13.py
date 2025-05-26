from collections import deque

d = deque([91, 97, 33])
d.append(-16)
# d.appendleft(100)
d.append(99)
for _ in range(len(d)):
    print(d.popleft())