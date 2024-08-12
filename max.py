class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        
        # Recursively calculate the maximum gain from left and right subtrees
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Current maximum path would include the node itself plus the max gain from both subtrees
        current_max_path = node.val + left_gain + right_gain
        
        # Update the global maximum sum
        max_sum = max(max_sum, current_max_path)
        
        # Return the maximum gain that can be obtained from the node to its parent
        return node.val + max(left_gain, right_gain)
    
    max_sum = float('-inf')
    max_gain(root)
    return max_sum

# Constructing the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Finding the maximum path sum
print(max_path_sum(root))  # Output will be the maximum path sum
