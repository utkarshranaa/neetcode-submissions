# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiameter=0
        def dfs(node):

            if node == None:
                return 0

            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)

            curr_diameter= left_subtree +right_subtree

            self.maxdiameter = max(curr_diameter , self.maxdiameter)

            return max(left_subtree, right_subtree) +1

        dfs(root)

        return self.maxdiameter        