import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value, priority=0):
        heapq.heappush(self.queue, (priority, value))
    
    def dequeue(self):
        return heapq.heappop(self.queue)[1] if self.queue else None

