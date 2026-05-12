class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkmirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return (left.val == right.val and 
            checkmirror(left.left, right.right) and 
            checkmirror(left.right, right.left))

        return checkmirror(root, root)