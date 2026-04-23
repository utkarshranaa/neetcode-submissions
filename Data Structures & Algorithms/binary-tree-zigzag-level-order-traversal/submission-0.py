from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        queue = deque([root])
        result = []
        is_reverse = False

        while len(queue)>0:
            l= len(queue)
            curr_level= []

            for _ in range(l):
                node = queue.popleft()
                curr_level.append(node.val)

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                
            if is_reverse == True:
                curr_level.reverse()
            
            result.append(curr_level)

            is_reverse= not is_reverse

        return result


        
        