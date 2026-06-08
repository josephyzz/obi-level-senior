"""
LIFO: (Last in First Out)
"""

import queue

pilha = queue.LifoQueue()
pilha.put(1)
pilha.put(2)
pilha.put(3)

print(pilha.get())

# O get ele já remove o item da pilha
