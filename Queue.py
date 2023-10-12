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

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue("Pavan")
queue.enqueue("Krishna")
queue.enqueue("Siva")
print(queue.front())    
print(queue.dequeue())  
print(queue.dequeue())
print((queue.size())) 
print(queue.front()) 
print(queue.dequeue())
print(queue.front())  
