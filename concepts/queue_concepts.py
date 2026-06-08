"""
Queue: FIFO (First-In-First-Out)
LifoQueue: LIFO (Last-In-First-Out)
PriorityQueue: Segue o conceito de “ordem de prioridade”.
Se os elementos da fila têm prioridades diferentes, então o elemento com alta prioridade é extraído primeiro.
"""

import queue

# First-In-First-Out
fila_fifo = queue.Queue()
fila_fifo.put(1)
fila_fifo.put(2)
print(fila_fifo.get())

# Last-In-First-Out
fila_lifo = queue.LifoQueue()
fila_lifo.put(1)
fila_lifo.put(3)
print(fila_lifo.get())

# PriorityQueue
fila_prioridade = queue.PriorityQueue()
fila_prioridade.put((2, 'Primeiro da fila'))
fila_prioridade.put((1, 'Segunda da fila'))

print(fila_prioridade.get())
