class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        

def find_center(node):
    slow, fast = node, node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


node = Node(1, Node(2, Node(3)))
node2 = Node(1, Node(2, Node(3, Node(4))))

result = find_center(node)
result2 = find_center(node2)

print(result.value)
print(result2.value)