import collections 
import queue
sam = [1,3,4,4,4,4,42,2,2,2,7,8,9,7,7]
a = collections.deque()
b = queue.LifoQueue()
a.append(19)
print(a)
b.put(88)
b.put(99)
b.get()
print(b.get())
