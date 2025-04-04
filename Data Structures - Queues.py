# Queues : It resembles the queue in the real-world
# It has the FIFO behavior - First In First Out

# So let's say we have a queue of three items, if you want to remove an item from this, you should remove the one at the beginning as opposed to the one at the end
[1, 2, 3]

from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()   # to remove an item from the beginning of the queue we call popleft()
print(queue)  # output : deque([2, 3])

# Also similar to the list, we can also check if the queue is empty using the not operator
if not queue:
    print("empty")
