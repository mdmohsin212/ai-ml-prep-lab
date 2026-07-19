class Solution:
    ans = 0
    def left_sum(self, root):
        if root == None:
            return
        if root.left:
            if root.left.left == None and root.left.right == None:
                self.ans += root.left.val
        
        self.left_sum(root.left)
        self.left_sum(root.right)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.left_sum(root)
        return self.ans