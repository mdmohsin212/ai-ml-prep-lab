import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value, priority=0):
        heapq.heappush(self.queue, (priority, value))
    
    def dequeue(self):
        if self.queue:
            item = heapq.heappop(self.queue)
            return item[1]
        else:
            return None


pq = PriorityQueue()

pq.enqueue(100, priority=3)
pq.enqueue(200, priority=1)
pq.enqueue(300, priority=2)
pq.enqueue(400, priority=5)
pq.enqueue(500, priority=0)

print("Dequeue:", pq.dequeue())
print("Dequeue:", pq.dequeue())
print("Dequeue:", pq.dequeue())
print("Dequeue:", pq.dequeue())
print("Dequeue:", pq.dequeue())
print("Dequeue:", pq.dequeue())