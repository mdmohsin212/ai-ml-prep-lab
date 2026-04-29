class Hashmap:
    def __init__(self):
        self.size = 1000
        self.map = [None] * self.size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        key_hash = self._hash(key)
        self.map[key_hash] = value
    
    def get(self, key):
        key_hash = self._hash(key)
        return self.map[key_hash]
    
    def remove(self, key):
        key_hash = self._hash(key)
        self.map[key_hash] = None
        

marks = Hashmap()

marks.put(101, 85)
marks.put(102, 90)
marks.put(103, 78)

print("Student 101 Marks:", marks.get(101))
print("Student 102 Marks:", marks.get(102))
print("Student 103 Marks:", marks.get(103))

marks.remove(102)

print("Student 102 Marks After Remove:", marks.get(102))