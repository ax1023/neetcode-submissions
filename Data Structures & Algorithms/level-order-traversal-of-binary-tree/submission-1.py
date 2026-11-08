# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = [[root.val]]

        queue = deque([[root]])

        while queue:
            level_i = []
            nodes = []
            for i in queue.popleft():
                if i.left:
                    level_i.append(i.left.val)
                    nodes.append(i.left)
                if i.right:
                    level_i.append(i.right.val)
                    nodes.append(i.right)
            if level_i:
                res.append(level_i)
                queue.append(nodes)


        return res



        