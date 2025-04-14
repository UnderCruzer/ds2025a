from queue import Queue

q = Queue()
q.put("data structure")
q.put("da")
q.put("java")
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())