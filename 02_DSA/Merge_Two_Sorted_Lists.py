class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_list(l1, l2):
    dummy = Node(0)
    current = dummy
    
    while l1 and l2:
        if l1.value < l2.value:
            current.next, l1 = l1, l1.next
        else:
            current.next, l2 = l2, l2.next
            
        current = current.next
    
    current.next = l1 or l2
    return dummy.next

def print_list(node):
    values = []
    while node:
        values.append(node.value)
        node = node.next
    print(values) 


l1 = Node(1, Node(2, Node(4)))
l2 = Node(1, Node(3, Node(5)))

merged_list = merge_sorted_list(l1, l2)
print_list(merged_list)