class Queue: # FIFO
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, value):
        self.stack1.append(value)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None
    
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())

queue.enqueue(40)
queue.enqueue(50)

print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())