class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


stask = Stack()

print(stask.is_empty())
stask.push(1)
stask.push(2)
stask.push(3)
print(stask.is_empty())
print(stask.peek())
