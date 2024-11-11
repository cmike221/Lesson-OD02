class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Пример использования стека
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)  # [1, 2, 3]
print(stack.pop())  # 3
print(stack)  # [1, 2]
