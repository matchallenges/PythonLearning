# first in, first out list

from collections import deque

queue = deque(['Mathieu', 'Sam', 'Harry'])
queue.append('Micheal')
queue.append('Filbert')

print(queue)

print(queue.popleft()) # Mathieu leaves

print(queue.popleft()) # Sam leaves

print(queue)

