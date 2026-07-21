from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data: OrderedDict[int, int] = OrderedDict()
        
    
    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        
        self.data.move_to_end(key)
        return self.data[key]
    
    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)
            

cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))

cache.put(3, 30)

print(cache.get(2))
print(cache.get(3))

cache.put(4, 40)

print(cache.get(1))
print(cache.get(3))
print(cache.get(4))