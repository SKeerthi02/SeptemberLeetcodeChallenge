class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.answer = 0
        
        def helper(node, value):
            if node:
                value += str(node.val)
                if not (node.left or node.right):
                    self.answer += int(value, 2)

                helper(node.left, value)
                helper(node.right, value)
                print(value)
        helper(root, "")
        return self.answer
