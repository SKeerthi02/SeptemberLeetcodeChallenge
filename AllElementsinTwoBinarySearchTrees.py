class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        array1 = []
        array2 = []
        
        
        def inorder(node, array):
            
            if node:
                inorder(node.left, array)
                array.append(node.val)
                inorder(node.right, array)
            
        
        inorder(root1, array1)
        inorder(root2, array2)
        
        return sorted(array1 + array2)
