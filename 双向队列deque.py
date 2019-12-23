from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.appendleft([10, 20, 30])
print(dq)
dq.append([50, 11, 22])
print(dq)
dq.extend([10, 20, 30])
print(dq)
dq.extendleft([10, 20, 30])
print(dq)
print(dq[2])
