class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from an empty queue")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Пример использования очереди
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)  # [1, 2, 3]
print(queue.dequeue())  # 1
print(queue)  # [2, 3]
