class StackNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        self.top = StackNode(value, self.top)
    
    def pop(self):
        if not self.top:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        return None if not self.top else self.top.value
    
    def is_empty(self):
        return self.top is None
    
    
stack = Stack()

print("Is empty:", stack.is_empty())

stack.push(10)
stack.push(20)
stack.push(30)

print("Top value:", stack.peek())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Top value:", stack.peek())

stack.push(40)

print("Top value:", stack.peek())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Is empty:", stack.is_empty())