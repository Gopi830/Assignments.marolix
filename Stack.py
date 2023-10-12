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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()
stack.push("Raj")
stack.push("Nikhil")
stack.push("Gopi")
print(stack.peek())  
print(stack.pop())   
print(stack.pop())
print(stack.pop())
print(stack.size())
print(stack.peek())
