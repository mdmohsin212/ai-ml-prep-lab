class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree = {}
        child = set()

        for parent_val, child_val, is_left in descriptions:

            if parent_val not in tree:
                tree[parent_val] = TreeNode(parent_val)

            if child_val not in tree:
                tree[child_val] = TreeNode(child_val)

            if is_left:
                tree[parent_val].left = tree[child_val]
            else:
                tree[parent_val].right = tree[child_val]

            child.add(child_val)

        for node_val in tree:
            if node_val not in child:
                return tree[node_val]