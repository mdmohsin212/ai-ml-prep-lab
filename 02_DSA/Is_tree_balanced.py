class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

def if_balanced(root):
    def check_balance(node):
        if not node:
            return 0, True
        
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)
        
        return max(left_height, right_height) + 1, left_balanced and right_balanced and abs(left_height - right_height) <= 1
    
    return check_balance(root)[1]


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.left = node2
node1.right = node3
node3.right = node4

print(if_balanced(node1))