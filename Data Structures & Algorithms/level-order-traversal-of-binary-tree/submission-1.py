from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = {}
        nodes = deque()
        ans = []
        if root is None:
            return ans
        nodes.append(root)
        while nodes:
            temp = []
            for _ in range(len(nodes)):
                x = nodes.popleft()
                if x.left:
                    nodes.append(x.left)
                if x.right:
                    nodes.append(x.right)
                temp.append(x.val)
            ans.append(temp)
        
        return ans